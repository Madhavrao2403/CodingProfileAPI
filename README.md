# 👨‍💻 CodingProfileAPI

A simple Flask-based API that fetches coding profile data (currently supports HackerRank) such as badges, stars, and solved problems. Built to be lightweight and extendable.

## 🚀 Features

- ✅ Fetch HackerRank badges for a user
- ✅ Retrieve stars, rank, solved challenges, and total challenges
- 🔧 Easily extendable to include other platforms like LeetCode, Codeforces, etc.

## 🛠 Tech Stack

- Python 3.7.4
- Flask
- Requests

## 📦 API Endpoint

### `GET /hackerrank`

**Query Parameters:**
- `username`: HackerRank username (required)

**Example Request:**
