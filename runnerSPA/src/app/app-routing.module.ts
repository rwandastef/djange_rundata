import { HomePageComponent } from './specialPages/HomePage/HomePage.component';
import { LandingPageComponent } from './specialPages/landingPage/landingPage.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
  { path: '', component: LandingPageComponent},
  { path: 'home', component: HomePageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
