import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { environment } from '../environments/environment';
import { Todo } from './todo';

@Injectable()
export class TodosService {

  constructor(private _httpClient: HttpClient) { }

  getTodos(): Observable<Todo[]> {
    return this._httpClient.get<Todo[]>(`${environment.api}/todos`);
  }

}
