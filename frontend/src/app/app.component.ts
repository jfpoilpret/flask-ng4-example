import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs/Observable';

import { Todo } from './todo';
import { TodosService } from './todos.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  todos$: Observable<Todo[]>;

  constructor(private _todosService: TodosService) { }

  ngOnInit(): void {
    this.todos$ = this._todosService.getTodos();
  }
}
