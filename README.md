# Movie Reservation System

## Overview
This project is a **Movie Reservation System** designed to streamline the process of managing movies, showtimes, and seat reservations. It offers a user-friendly interface for regular users to reserve seats and an administrative dashboard for admins to manage movies, reservations, and system reports.

---

## Features

### 1. **User Authentication and Authorization**
- **Sign-Up and Login**: Users can create accounts and log in to access the system.
- **Roles**: 
  - **Admin**: Manages movies, showtimes, reservations, and generates reports.
  - **Regular User**: Reserves seats and manages personal reservations.
- **Admin Privileges**:
  - Promote users to admin.
  - Perform all administrative operations.

### 2. **Movie Management** (Admin-only)
- **CRUD Operations**: Add, update, and delete movies.
- **Movie Details**:
  - Title
  - Description
  - Poster image
  - Genre
- **Showtimes**: Assign and manage showtimes for movies.

### 3. **Reservation Management**
- **For Users**:
  - View movies and showtimes for a specific date.
  - Reserve seats for a selected showtime.
  - See available seats.
  - View and cancel reservations.
- **For Admins**:
  - Access all reservation records.
  - Monitor seat availability and overall capacity.


---

## Requirements

### **System Requirements**
- **Python**: v3.8+
- **Django**: v4.0+
- **Database**: SQLite (default)

### **Functional Requirements**
1. **User Authentication**:
   - Secure login and sign-up system.
   - Differentiate roles with distinct permissions.
2. **Admin Operations**:
   - Seed initial admin data.
   - Enable admin promotions.
3. **Movie and Showtime Management**:
   - CRUD operations for movies and showtimes.
4. **Reservation Management**:
   - Track, reserve, and cancel seats.
   - Display available seats for specific showtimes.

---

## Project Page

You can view the project roadmap and details at: [Movie Reservation System Roadmap](https://roadmap.sh/projects/movie-reservation-system)

---

## Installation

1. Clone the repository:
   ```bash
   git clone  https://github.com/Hcode7/Movie-Reservation-System.git
   
