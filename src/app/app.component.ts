import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Verifica {
  id: string;
  corso: string;
  titolo: string;
  tipo: string;
  difficolta: string;
  durata: Date;
  scariche: number;
  testo_url: string;
  griglia_di_valutazione_url: string;
  data_ideazione: Date;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  obsQuery1: Observable<Verifica[]>;
  listVerifica: Verifica[];
  nomeDocente: string = '';
  cognomeDocente: string = '';

  constructor(public http: HttpClient) { }

  getVerifiche(nome: HTMLInputElement, cognome: HTMLInputElement) {
    this.obsQuery1 = this.http.get<Verifica[]>(
      `http://localhost:5000/api/query1?nome=${nome.value}&cognome=${cognome.value}`
    );
    this.obsQuery1.subscribe((data) => (this.listVerifica = data));
  }
}
