from apify_client import ApifyClient
import csv

# Inisialisasi client dengan API key
client = ApifyClient("apify_api_yh7RPOpiv0yMjhBDRghRgSJYsNymLk44ipQj")

# Masukkan semua link Reddit yang ingin di-scrape
run_input = {
    "startUrls": [
        { "url": "https://www.reddit.com/r/NintendoSwitch/comments/1l8yu8u/my_experience_so_far_with_nintendo_switch_2/" },
        { "url": "https://www.reddit.com/r/NintendoSwitch2/" },
        { "url": "https://www.reddit.com/r/NintendoSwitch/comments/1k8rt70/my_switch_2_preview_impressions_software_and/" },
        { "url": "https://www.reddit.com/r/NintendoSwitch/comments/1lcxq6n/the_switch_2_is_equally_amazing_frustrating/" },
        { "url": "https://www.reddit.com/r/NintendoSwitch/" }



    ],
    "sort": "new",
    "maxItems": 100,
    "maxPostCount": 100,
    "maxComments": 100,
    "scrollTimeout": 40,
    "proxy": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"],
    },
}

# Jalankan aktor Apify
run = client.actor("trudax/reddit-scraper-lite").call(run_input=run_input)

# Tampilkan link dataset
print("💾 Data tersedia di: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])

# Ambil hanya komentar dari dataset
comments = [
    item for item in client.dataset(run["defaultDatasetId"]).iterate_items()
    if item["dataType"] == "comment"
]

# Simpan komentar ke file CSV
with open("apifylink.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["username", "body", "upVotes"])
    writer.writeheader()
    for item in comments:
        writer.writerow({
            "username": item["username"],
            "body": item["body"],
            "upVotes": item["upVotes"]
        })

print("✅ CSV berhasil disimpan sebagai apifylink.csv")
