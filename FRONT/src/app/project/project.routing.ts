import { Routes, RouterModule } from '@angular/router';

import { ProjectComponent } from './project.component';
import { AuthGuard } from '../shared/auth.guard';

const PROFILE_ROUTES: Routes = [
  { path: '', component: ProjectComponent, canActivate: [AuthGuard] }
];

export const ProjectRouting = RouterModule.forChild(PROFILE_ROUTES);
