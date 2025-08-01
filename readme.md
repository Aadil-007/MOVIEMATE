# 🎬 MovieMate

<div align="center">

<img width="528" height="169" alt="Screenshot 2025-08-01 224445" src="https://github.com/user-attachments/assets/d2c29200-c52e-4fc7-b8db-aa5931ca40da" />


**Your personal movie and TV show collection manager with AI-powered features**


</div>

## ✨ Features

### 🎯 **Core Functionality**
- 🎬 **Movie & TV Show Management** - Add, edit, and organize your entertainment collection
- 📊 **Progress Tracking** - Track episodes watched, seasons, and completion percentage
- ⭐ **Rating & Reviews** - Rate content (1-10) and write detailed reviews
- 🔍 **Advanced Filtering** - Filter by genre, platform, status, and more
- 📈 **Statistics Dashboard** - View your watching statistics and progress

### 🤖 **Smart Features**
- 🔍 **OMDB API Integration** - Auto-fetch movie details, posters, and metadata
- 🎯 **Smart Platform Detection** - Automatically suggests streaming platforms
- 📝 **Auto-Generated Reviews** - AI-powered review suggestions from plot summaries
- ⚡ **One-Click Auto-Fill** - Complete movie information with a single click

### 🎨 **Modern UI/UX**
- 🌙 **Black Glass Theme** - Stunning dark mode with glass morphism effects
- 📱 **Fully Responsive** - Perfect experience on desktop, tablet, and mobile
- ✨ **Smooth Animations** - Engaging micro-interactions and transitions
- 🎭 **Status-Based Visual Indicators** - Color-coded cards for different statuses

## 🚀 Quick Start

### Prerequisites

- Node.js 16.0+ 
- npm
- Supabase account
- OMDB API key (free at [omdbapi.com](http://www.omdbapi.com/))

### Installation

1. **Clone the repository**
   
```bash
git clone https://github.com/yourusername/moviemate.git
cd moviemate
```

3. **Install dependencies**
```bash 
npm install
```

5. **Set up environment variables**

Create a `.env.local` file in the `frontend` directory:
```bash
REACT_APP_SUPABASE_URL=your-supabase-project-url
REACT_APP_SUPABASE_ANON_KEY=your-supabase-anon-key
```

4. **Set up the database**

Run this SQL in your Supabase SQL Editor:
```bash
 Create movies table
CREATE TABLE movies (
id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
title text NOT NULL,
director text,
genre text,
platform text DEFAULT 'Netflix',
status text DEFAULT 'wishlist',
rating real,
review text,
poster_url text,
year integer,
created_at timestamptz DEFAULT now(),
updated_at timestamptz DEFAULT now()
);

-- Create tvshows table
CREATE TABLE tvshows (
id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
title text NOT NULL,
director text,
genre text,
platform text DEFAULT 'Netflix',
status text DEFAULT 'wishlist',
rating real,
review text,
poster_url text,
year integer,
total_episodes integer,
episodes_watched integer DEFAULT 0,
current_season integer DEFAULT 1,
total_seasons integer,
created_at timestamptz DEFAULT now(),
updated_at timestamptz DEFAULT now()
);

-- Add constraints for data integrity
ALTER TABLE movies ADD CONSTRAINT movies_status_check
CHECK (status IN ('wishlist', 'watching', 'completed'));

ALTER TABLE tvshows ADD CONSTRAINT tvshows_status_check
CHECK (status IN ('wishlist', 'watching', 'completed'));

-- Refresh schema cache
NOTIFY pgrst, 'reload schema';

```


5. **Start the development server**
   
```bash
cd frontend
npm start
```

6. **Open your browser**

Navigate to `http://localhost:3000` and start building your collection! 🎉


Screenshots :
web interface:
<img width="1910" height="863" alt="image" src="https://github.com/user-attachments/assets/c48210b8-eddc-4027-93bc-dbe2ad479ebf" />

<img width="1729" height="438" alt="image" src="https://github.com/user-attachments/assets/a2931da7-a8e3-4116-a59d-c543745ea64e" />

<img width="1767" height="851" alt="image" src="https://github.com/user-attachments/assets/9f24f68d-9d74-40b4-81e7-5ecfc7482da0" />

database table schema visualizer :
<img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/a4cd8789-af83-47df-8d81-952cad25c22b" />





