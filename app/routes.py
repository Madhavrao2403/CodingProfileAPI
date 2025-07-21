from flask import Blueprint, request, jsonify
import requests

hackerrank_bp = Blueprint("hackerrank", __name__)

@hackerrank_bp.route("/hackerrank", methods=["GET"])
def get_hackerrank_badge():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username parameter is required"}), 400

    url = f"https://www.hackerrank.com/rest/hackers/{username}/badges"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("status") and "models" in data:
            badges = data["models"]

            # Use a dict to store unique badges by badge_name
            unique_badges = {}

            for badge in badges:
                badge_name = badge.get("badge_name")
                if badge_name and badge_name not in unique_badges:
                    unique_badges[badge_name] = {
                        "username": username,
                        "badge_name": badge_name,
                        "stars": badge.get("stars", 0),
                        "rank": badge.get("hacker_rank", "Not Available"),
                        "solved": badge.get("solved", 0),
                        "total": badge.get("total_challenges", 0)
                    }

            return jsonify({"models": list(unique_badges.values())})
        else:
            return jsonify({"error": "No badge data found for this user."}), 404
    else:
        return jsonify({"error": f"Failed to fetch data: HTTP {response.status_code}"}), response.status_code
