import { AnalysedUitslagenComponent } from './uitslagen/analysedUitslagen/analysedUitslagen.component';
import { SingleDigitComponent } from './startnummers/SingleDigit/SingleDigit.component';
import { WeerregressieComponent } from './weeer/weerregressie/weerregressie.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { WeerListComponent } from './weeer/WeerList/WeerList.component';
import { AuthenticationService } from './_services/Authentication.service';
import { HeaderComponent } from './layout/Header/Header.component';
import { FooterComponent } from './layout/Footer/Footer.component';
import { HomePageComponent } from './specialPages/HomePage/HomePage.component';
import { LandingPageComponent } from './specialPages/landingPage/landingPage.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule} from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';


//material imports
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';

@NgModule({
  declarations: [
    AppComponent,

    // layout
    LandingPageComponent,
    HomePageComponent,
    FooterComponent,
    HeaderComponent,
    WeerListComponent,
    WeerregressieComponent,
    SingleDigitComponent,
    AnalysedUitslagenComponent

  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    MatTableModule,
    MatPaginatorModule
  ],
  providers: [
    AuthenticationService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
