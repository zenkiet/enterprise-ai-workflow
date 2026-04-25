# SKILL: angular-scaffold

## Purpose

This skill generates clean, production-ready Angular code scaffolds based on an approved `plan.md`. It strictly enforces Smart/Dumb component separation, declarative patterns, and shared-first principles. The output is a working skeleton — Kiet's team fills in the business logic.

**Only activate after `task-intake` has produced an approved plan.**

---

## Core Principles (Non-Negotiable)

These rules apply to every single file generated. No exceptions.

| Principle                       | Rule                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Smart/Dumb Separation**       | Smart = container (data, services, state). Dumb = presentational (@Input/@Output only). Never mix.                 |
| **Declarative over Imperative** | Use `async` pipe, `signal()`, `computed()`, `toSignal()`. No manual `.subscribe()` without `takeUntilDestroyed()`. |
| **Shared-First**                | Always check `shared/` before creating. If reusable → create in `shared/`.                                         |
| **Minimal Code**                | No dead code. No placeholder comments. No `TODO` unless explicitly requested. No unnecessary imports.              |
| **OnPush by Default**           | All Dumb components use `ChangeDetectionStrategy.OnPush`. Smart components may use Default only if justified.      |
| **Standalone Components**       | Use `standalone: true` unless the project's `.agent/RULES.md` specifies otherwise.                                 |
| **No Magic Strings**            | Enums or constants for repeated string values.                                                                     |

---

## Step-by-Step Procedure

### Step 0 — Guideline Check

Before writing any file, re-run the checkpoints from [.agent/GUIDELINES.md](../../.agent/GUIDELINES.md):

- **Think:** re-read the approved `plan.md`. Every file you are about to create must already be listed there. If something is missing → stop, update the plan, re-approve.
- **Simplify:** generate the minimum code that satisfies the plan. No placeholder methods "for later". No configurability that was not requested.
- **Surgical:** each file in `Files to Create` / `Files to Modify` must trace to the plan. Reject anything speculative. Do not touch adjacent files.
- **Goal-Driven:** know how you will verify the scaffold (Step 8 `tsc --noEmit` + lint). If the plan has a stricter success criterion, match it.

If any checkpoint fails → halt, report in Slack, do not scaffold.

See [skills/guideline/SKILL.md](../guideline/SKILL.md) §Checkpoint 2 and §Checkpoint 3 for the full question set.

---

### Step 1 — Load Context

Read the approved `plan.md` and confirm:

- Project name and directory
- Files to create (from plan)
- Files to modify (from plan)
- Shared components to reuse (from plan)
- Architecture notes (from plan)

Also re-confirm `.agent/ARCHITECTURE.md` and `.agent/RULES.md` are loaded for this session.

---

### Step 2 — Scaffold Smart Component

The Smart Component is the container. It owns data fetching, state, and service calls.

**Template:**

```typescript
// [name].component.ts
import { Component, inject, OnInit } from '@angular/core';
import { CommonModule, AsyncPipe } from '@angular/common';
import { Observable } from 'rxjs';
import { [Name]UiComponent } from './[name]-ui/[name]-ui.component';
import { [Name]Service } from './[name].service';
import { [ModelType] } from './[name].model';

@Component({
  selector: 'app-[name]',
  standalone: true,
  imports: [CommonModule, AsyncPipe, [Name]UiComponent],
  template: `
    <app-[name]-ui
      [data]="data$ | async"
      (action)="onAction($event)">
    </app-[name]-ui>
  `,
})
export class [Name]Component implements OnInit {
  private readonly [name]Service = inject([Name]Service);

  data$: Observable<[ModelType][]> = this.[name]Service.getAll();

  ngOnInit(): void {
    // initialization logic if needed
  }

  onAction(event: [EventType]): void {
    // delegate to service
  }
}
```

**Rules for Smart Component:**

- Use `inject()` — never constructor injection
- Use `readonly` for injected services
- Expose streams as `Observable<T>` or `Signal<T>` — never raw data
- Keep template minimal — delegate all UI to Dumb component
- No direct DOM manipulation

---

### Step 3 — Scaffold Dumb Component

The Dumb Component is purely presentational. It receives data via `@Input` and communicates via `@Output`.

**Template:**

```typescript
// [name]-ui/[name]-ui.component.ts
import {
  Component,
  Input,
  Output,
  EventEmitter,
  ChangeDetectionStrategy,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { [ModelType] } from '../[name].model';

@Component({
  selector: 'app-[name]-ui',
  standalone: true,
  imports: [CommonModule],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <!-- UI template here -->
    <div *ngIf="data; else loading">
      <!-- render data -->
    </div>
    <ng-template #loading>
      <!-- loading state -->
    </ng-template>
  `,
})
export class [Name]UiComponent {
  @Input() data: [ModelType][] | null = null;
  @Output() action = new EventEmitter<[EventType]>();

  onAction(value: [EventType]): void {
    this.action.emit(value);
  }
}
```

**Rules for Dumb Component:**

- `ChangeDetectionStrategy.OnPush` — always
- `@Input()` for all data — never inject services
- `@Output()` for all user actions — never call services directly
- `null` as default for nullable inputs (compatible with `async` pipe)
- No business logic — only display logic (formatting, conditional rendering)

---

### Step 4 — Scaffold Service (if needed)

Only create a service if the plan explicitly requires business logic or API integration.

**Template:**

```typescript
// [name].service.ts
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { [ModelType] } from './[name].model';

@Injectable({
  providedIn: 'root',
})
export class [Name]Service {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = '/api/[endpoint]';

  getAll(): Observable<[ModelType][]> {
    return this.http.get<[ModelType][]>(this.baseUrl).pipe(
      map((response) => response),
      catchError((error) => {
        // handle error
        throw error;
      })
    );
  }

  getById(id: string): Observable<[ModelType]> {
    return this.http.get<[ModelType]>(`${this.baseUrl}/${id}`);
  }

  create(data: Partial<[ModelType]>): Observable<[ModelType]> {
    return this.http.post<[ModelType]>(this.baseUrl, data);
  }

  update(id: string, data: Partial<[ModelType]>): Observable<[ModelType]> {
    return this.http.put<[ModelType]>(`${this.baseUrl}/${id}`, data);
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
```

**Rules for Services:**

- `providedIn: 'root'` unless scoped to a feature module
- Use `inject()` — never constructor injection
- Return `Observable<T>` — never subscribe inside service
- Handle errors with `catchError` — never swallow silently
- One service per feature — no god services

---

### Step 5 — Scaffold Model (if needed)

Create a model file if the plan involves typed data structures.

**Template:**

```typescript
// [name].model.ts
export interface [ModelType] {
  id: string;
  // add fields based on API/Jira spec
  createdAt: Date;
  updatedAt: Date;
}

export type [ModelType]CreateDto = Omit<[ModelType], 'id' | 'createdAt' | 'updatedAt'>;
export type [ModelType]UpdateDto = Partial<[ModelType]CreateDto>;
```

---

### Step 6 — Scaffold Shared Utilities (if needed)

If the plan identifies a reusable utility that doesn't exist in `shared/`, create it there.

**Pipe template:**

```typescript
// shared/pipes/[name].pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: '[camelCaseName]',
  standalone: true,
  pure: true,
})
export class [Name]Pipe implements PipeTransform {
  transform(value: unknown, ...args: unknown[]): unknown {
    // transformation logic
    return value;
  }
}
```

**Directive template:**

```typescript
// shared/directives/[name].directive.ts
import { Directive, Input, HostBinding } from '@angular/core';

@Directive({
  selector: '[app[Name]]',
  standalone: true,
})
export class [Name]Directive {
  @Input('app[Name]') value: unknown;
}
```

After creating in `shared/`, update `.agent/SKILL.md` with the new entry.

---

### Step 7 — Update Routing (if needed)

If the plan requires adding a new route, update the routing file:

```typescript
// In the relevant routing file
{
  path: '[route-path]',
  loadComponent: () =>
    import('./features/[name]/[name].component').then(
      (m) => m.[Name]Component
    ),
},
```

Always use lazy loading (`loadComponent`) for feature routes.

---

### Step 8 — Verify Generated Files

Before handing off to `git-workflow`, verify:

```bash
# Check TypeScript compiles
npx tsc --noEmit

# Check for lint errors (if eslint configured)
npx eslint src/app/features/[name]/ --ext .ts

# Dry-run to confirm file structure
find src/app/features/[name] -type f | sort
find src/app/shared -newer src/app/shared/.gitkeep -type f | sort
```

If compilation errors exist, fix them before proceeding.

---

## File Naming Conventions

| Type            | Pattern                  | Example                       |
| --------------- | ------------------------ | ----------------------------- |
| Smart Component | `[name].component.ts`    | `user-list.component.ts`      |
| Dumb Component  | `[name]-ui.component.ts` | `user-list-ui.component.ts`   |
| Service         | `[name].service.ts`      | `user-list.service.ts`        |
| Model           | `[name].model.ts`        | `user.model.ts`               |
| Pipe            | `[name].pipe.ts`         | `date-format.pipe.ts`         |
| Directive       | `[name].directive.ts`    | `highlight.directive.ts`      |
| Spec            | `[name].spec.ts`         | `user-list.component.spec.ts` |

All files use **kebab-case**. All classes use **PascalCase**. All selectors use `app-` prefix.

---

## What NOT to Generate

- No `ngOnDestroy` with manual `Subject` + `takeUntil` — use `takeUntilDestroyed()` instead
- No `constructor` injection — use `inject()` instead
- No `any` types — always type explicitly
- No inline styles — use TailwindCSS classes or component stylesheet
- No `console.log` — use proper error handling
- No barrel files (`index.ts`) unless the project's `.agent/RULES.md` requires them
- No `ngModule` unless the project explicitly uses module-based architecture

---

## Memory

After each scaffold, log to `memory/YYYY-MM-DD.md`:

```markdown
## [HH:MM] Scaffold — [Task Title]

- Project: [name]
- Files created: [list]
- Files modified: [list]
- Shared components reused: [list]
- New shared utilities created: [list]
- Notes: [anything unusual — patterns discovered, edge cases]
```

Also update `.agent/SKILL.md` in the project if new shared utilities were created.
