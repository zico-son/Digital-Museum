# Digital Museum Project Backend

Welcome to the Digital Museum Project Backend — a Django-powered solution envisioned to revamp traditional museum experiences into a digitized, interactive, and user-friendly platform.

## 🤔 Problem Definition

In a conventional museum setup, visitors often encounter challenges such as prolonged ticket queues, limited insights on exhibits, and the lack of an engaging platform to explore artworks in depth. Our initiative resolves these issues by introducing a digitized platform that affords detailed museum insights, facilitates effortless ticket booking, and houses an interactive art hub to augment the visitor's experience.

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Technical Stack](#technical-stack)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Admin Panel](#admin-panel)
- [API Endpoints](#api-endpoints)
- [License](#license)

## 🖼 Project Overview

Our backend concentrates on ensuring a smooth user journey by segregating functionalities into three pivotal apps, each addressing particular challenges:

### Ticket Booking

#### Problem
Traditional ticket booking avenues are generally time-consuming, leading to extensive queues that dampen the visitor experience.

#### Solution
The Ticket Booking app substantially alleviates this bottleneck, granting users the convenience of home-based ticket bookings. Features encompass:
- **Online Booking**: A feature allowing bookings via diverse payment gateways.
- **Booking Management**: A facility to manage bookings, inclusive of viewing booking history and executing cancellations.
- **Notifications**: An automated system to forward booking confirmations, reminders, and cancellation alerts through email.

### Museum Info

#### Problem
A substantial number of visitors find themselves with restricted access to exhaustive details on exhibits, events, and the ingrained history of the museum, hindering a fully immersive experience.

#### Solution
The Museum Info app operates as a vast repository of information, offering users an in-depth peek into various museum segments. Noteworthy functionalities are:
- **Exhibit Details**: A feature providing extensive details on each exhibit, inclusive of historical backgrounds and involved artifacts.
- **Event Calendar**: An updated calendar allowing users to track forthcoming events and exhibitions.
- **Museum History**: A segment devoted to narrating the rich history and legacy of the museum.

### Art Hub

#### Problem
Traditionally, museums offer limited scopes for visitors to engage interactively and learn about artworks and their creators in depth.

#### Solution
The Art Hub app innovates by fashioning an interactive arena where art aficionados can explore artworks meticulously. Prime features include:
- **High-Resolution Images**: An option to view artworks in high-resolution imagery.
- **Artist Biographies**: A section where users can familiarize themselves with the creators behind the artworks, their history, and portfolio.
- **Interactive Exhibits**: An immersive experience allowing users to interact digitally with exhibits, fostering a profound understanding of art pieces.

## 💻 Technical Stack

Leveraging a robust technical stack to guarantee top-notch performance and a pleasant user experience:
- **Backend Framework**: Django
- **Database**: AWS PostgreSQL for reliable and scalable data management
- **Storage**: AWS S3 for steadfast and scalable storage of static and media files
- **Email Services**: Integration with SendGrid for reliable email notifications and alerts
- **Image Optimization**: Adoption of webp format for image conversions, enhancing webpage loading time significantly.

## 🛠 Setup and Installation

### Prerequisites

Ensure your system houses the following prerequisites:
- Python (3.9 or higher)
- Django (4.2 or higher)
- PostgreSQL

### Installation

Adhere to the following instructions for a seamless local setup:

```bash
# Clone the repository
git clone https://github.com/zico-son/Digital-Museum.git

# Navigate to the project directory
cd digital-museum-backend

# Set up a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the necessary requisites
pip install -r requirements.txt

# Execute database setups
python manage.py migrate

# Run the server
python manage.py runserver
