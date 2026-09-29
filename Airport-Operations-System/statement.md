---

### 5. `statement.md`
```markdown
# Project Statement: Airport Management System (AMS)

## Problem Statement
Small-to-midsize flight hubs and simulated dispatch training setups frequently need a simple, low-overhead way to manage operational records without relying on bloated enterprise software or database servers. Manual spreadsheets result in data inconsistency and accidental overrides. This project provides a centralized, authenticated CLI solution for structured data management.

## Scope of the Project
- In-memory state tracking for Airlines, Flights, Passengers, and Employees.
- Role-gated authentication with strict retry limitations.
- Tabular display formatting and real-time compensation metrics.
- Excluded: External cloud database integration, network APIs, and web graphical interfaces.

## Target Users
- Airport operations coordinators and gate dispatchers.
- Passenger check-in and manifest clerks.
- Administrative staff handling ground workforce scheduling and compensation audits.

## High-Level Features
- Credential authentication gateway with lockout protection.
- Relational airline fleet and route registry.
- Live-updating flight timetable manifest.
- Unique-identifier passenger ticketing registry (PNR).
- HR payroll reporting module calculating mean, minimum, and maximum salaries.