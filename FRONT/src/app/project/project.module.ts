import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { ProjectComponent } from './project.component';
import { ProjectRouting } from './project.routing';
import { SharedModule } from '../shared/shared.module';

import { AngularFireDatabaseModule } from 'angularfire2/database';

@NgModule({
  declarations: [
    ProjectComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    SharedModule,
    ProjectRouting,
    AngularFireDatabaseModule
  ]
})
export class ProjectModule {}
