import { AuthenticationService } from './_services/Authentication.service';
import { HeaderComponent } from './layout/Header/Header.component';
import { FooterComponent } from './layout/Footer/Footer.component';
import { HomePageComponent } from './specialPages/HomePage/HomePage.component';
import { LandingPageComponent } from './specialPages/landingPage/landingPage.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,

    // layout
    LandingPageComponent,
    HomePageComponent,
    FooterComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    AuthenticationService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
