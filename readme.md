# 🎬 MovieMate

<div align="center">

![MovieMate Logo](https://via.placeholder.com/120x120/4ecdc4/ffffff?text=🎬)

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
- npm or yarn
- Supabase account
- OMDB API key (free at [omdbapi.com](http://www.omdbapi.com/))

### Installation

1. **Clone the repository**
'''bash 
git clone https://github.com/yourusername/moviemate.git
cd moviemate
'''
2. **Install dependencies**
'''bash 
npm install
'''

4. **Set up environment variables**

Create a `.env.local` file in the `frontend` directory:
REACT_APP_SUPABASE_URL=your-supabase-project-url
REACT_APP_SUPABASE_ANON_KEY=your-supabase-anon-key

4. **Set up the database**

Run this SQL in your Supabase SQL Editor:
'''bash
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
'''


5. **Start the development server**
   '''bash
cd frontend
npm start
'''

text

6. **Open your browser**

Navigate to `http://localhost:3000` and start building your collection! 🎉
