import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AngularFireModule } from 'angularfire2';
import { AngularFireAuthModule } from 'angularfire2/auth';



import { AppComponent } from './app.component';
import { routing } from './app.routing';
import { HeaderComponent } from './shared/header.component';
import { AuthService } from './shared/auth.service';
import { AuthGuard } from './shared/auth.guard';
import { NotAuthGuard } from './shared/notauth.guard';
import { HomeComponent } from './home.component';
import { AlertsService } from './shared/alerts/alerts.service';
import { AlertsComponent } from './shared/alerts/alerts.component';

export const firebaseConfig = {
  apiKey: 'AIzaSyA19i5xGl5mTcDBnCeTmUvjxG-5s9lq_hQ', /// This is a random test key. you need to change this API key to your API key.
  authDomain: 'spliceer-video.firebaseapp.com',
  databaseURL: 'https://spliceer-video.firebaseio.com',
  projectId: 'spliceer-video',
  storageBucket: 'spliceer-video.appspot.com',
  messagingSenderId: '564284062646'
};

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    AlertsComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AngularFireModule.initializeApp(firebaseConfig),
    AngularFireAuthModule,
    NgbModule.forRoot(),
    routing
  ],
  providers: [
    AuthService,
    AuthGuard,
    NotAuthGuard,
    AlertsService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
