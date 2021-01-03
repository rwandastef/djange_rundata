import { SingleDigitComponent } from './startnummers/SingleDigit/SingleDigit.component';
import { WeerregressieComponent } from './weeer/weerregressie/weerregressie.component';
import { WeerListComponent } from './weeer/WeerList/WeerList.component';
import { HomePageComponent } from './specialPages/HomePage/HomePage.component';
import { LandingPageComponent } from './specialPages/landingPage/landingPage.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
  { path: '', component: LandingPageComponent},
  { path: 'home', component: HomePageComponent},
  { path: 'weer', children: [{
      path: 'list',  component: WeerListComponent},
    { path: 'regression', component: WeerregressieComponent}]
  },
  { path: 'singledigit', component: SingleDigitComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
