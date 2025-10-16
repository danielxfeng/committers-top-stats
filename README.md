# 🇫🇮 GitHub Committers Top Stats

**Found out earlier that I ranked #1 in Finland for public commits 😜**  
Thanks to [Uygar Polat](https://github.com/uygarpolat) for pointing this out!

[committers.top](https://committers.top/) is a cool project that tracks the most active developers on GitHub by country — based on profile location, follower count (≥42 for Finland currently), and total contribution scores (top 256 per country).

I built a small tool to explore it further.

---

## 📊 Quick Insights

💻 **Average total contributions** across all countries: `1301`  
→ Finland ranks **27th** with `1963`
[!visual1](./visual/1.png)


🌍 **Share of public project commits** averages `35%`  
→ Finland ranks **25th** with `38%`
[!visual2](./visual/2.png)

🧩 **Commits as a percentage of total contributions** average `82%`  
→ Finland drops to **126th**, at `75%` — suggesting Finnish developers contribute relatively more through issues, PRs, and discussions than raw commits.
[!visual3](./visual/3.png)

---

## 🔍 K-Means Clustering

I ran a quick **K-Means clustering (k=5)** based on contribution features.  
Finland clusters with countries like:

> Argentina, Brazil, Denmark, Estonia, India, Singapore, Norway, Portugal, Ukraine, and others.

---

## 🧠 About the Project

This was just a small tool I built for fun — the data is rough and not meant to be taken too seriously 😄  
Also thanks to **AI**, I built this very fast 🤖  

You can play with it or explore your own patterns here.

---

## 🧰 Tech Stack

- Python (`pandas`, `matplotlib`, `scikit-learn`)
- K-Means clustering for pattern grouping
- Simple CSV-based data pipeline

---

## 💡 Install


Clone the repo and install dependencies:

```bash
git clone https://github.com/danielxfeng/committers-top-stats.git
cd committers-top-stats
pip install -r requirements.txt
```

---

✅ **License:** MIT
