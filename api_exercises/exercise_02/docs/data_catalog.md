# Data Catalog for the sources

This document shows the structure of each data source, including the columns and the data type of each column

### Posts Source

| Columns | Type   | Description                          | Relationship   | 
|---------|--------|--------------------------------------|----------------|
| userID  | INT    | ID of the user who created the post  | FK -> users.id |
| id      | INT    | Unique post identifier               | PK             |
| title   | String | Post title                           |                |
| body    | String | Post content                         |                |

---

### Comments Source

| Columns | Type   | Description                          | Relationship   | 
|---------|--------|--------------------------------------|----------------|
| postId  | INT    | ID of the post where the comment is  | FK -> posts.id |
| id      | INT    | Unique comment identifier            | PK             |
| name    | String | Name of who made the comment         |                |
| email   | String | Email of who made the comment        |                |
| body    | String | Comment content                      |                |

---

### Albums Source

| Columns | Type   | Description                          | Relationship   | 
|---------|--------|--------------------------------------|----------------|
| userId  | INT    |ID of the user that created the album | FK -> users.id |
| id      | INT    | Unique album identifier              | PK             |
| title   | String | Album title                          |                |

---

### Photos Source

| Columns     | Type   | Description                          | Relationship   | 
|-------------|--------|--------------------------------------|----------------|
| albumId     | INT    |ID of the user that created the album | FK -> albums.id|
| id          | INT    | Unique photo identifier              | PK             |
| title       | String | Photo title                          |                |
| url         | String | Photo URL                            |                |
| thumbnailUrl| String | Photo thumbnail                      |                |

---

### Todos Source

| Columns     | Type   | Description                          | Relationship   | 
|-------------|--------|--------------------------------------|----------------|
| userId      | INT    | ID of the user that created the task | FK -> users.id |
| id          | INT    | Unique task identifier               | PK             |
| title       | String | Task title                           |                |
| completed   | Boolean| Task status                          |                |

### Users Source

| Columns     | Type       | Description                          | Relationship   | 
|-------------|------------|--------------------------------------|----------------|
| id          | INT        | Unique user identifier               | PK             |
| name        | String     | User name                            |                |
| username    | String     | User username                        |                |
| email       | String     | User email                           |                |
| address     | Dictionary | User address                         |                |
| phone       | String     | User phone number                    |                |
| website     | String     | User website                         |                |
| company     | Dictionary | User company                         |                |