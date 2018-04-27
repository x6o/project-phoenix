import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

import { AuthService } from '../shared/auth.service';
import { AlertsService } from '../shared/alerts/alerts.service';

import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-tester1',
  templateUrl: './project.component.html',
  styles: []
})
export class ProjectComponent implements OnInit {
  itemsRef: AngularFireList<any>;
  items: Observable<any[]>;
  userEmail = '';
  alerts = [];
  requests: Observable<any[]>;
  userProjects = [];

  constructor(private authService: AuthService,
    private alertsService: AlertsService,
    private db:AngularFireDatabase
  ) { 
    this.itemsRef = db.list('requests');
    // Use snapshotChanges().map() to store the key
    this.items = this.itemsRef.snapshotChanges().map(changes => {
      return changes.map(c => ({ key: c.payload.key, ...c.payload.val() }));
    });
    
  }

  onNewProj(form: NgForm) {
    console.log("exec");
    this.itemsRef.push({ 
        playlistUrl: form.value.playlistUrl,
        numberVideos: form.value.numberVideos,
        videosFps: 30,
        pickRandom: true
    });

  }
  updateItem(key: string, newText: string) {
    this.itemsRef.update(key, { text: newText });
  }
  deleteItem(key: string) {    
    this.itemsRef.remove(key); 
  }
  deleteEverything() {
    this.itemsRef.remove();
  }

  onNewProj2(form: NgForm, db:AngularFireDatabase) {
    db.list('requests').push({playlistUrl: "oii11"});
  }

  ngOnInit() {
    this.authService.getMailAddress().first().subscribe(
      (email) => this.userEmail = email
    )
  }

}
