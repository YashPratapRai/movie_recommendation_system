import requests
import streamlit as st

# =============================
# CONFIG & EMBEDDED ENGINE
# =============================
API_BASE = "https://movie-recommendation-system-oy45.onrender.com"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="CineVerse Ultra | Next-Gen UI", 
    page_icon="🔮", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# HIGH-FIDELITY NEON STYLES
# =============================
st.markdown(
    """
    <style>
    /* Absolute Base Reset with Deep Violet Cyber Background */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #201635 0%, #0a0712 80%) !important;
        color: #f1f5f9 !important;
    }
    
    .block-container { 
        padding-top: 1.5rem; 
        padding-bottom: 4rem; 
        max-width: 1400px; 
    }
    
    /* Neon Branding Title */
    .brand-container {
        text-align: center;
        padding: 1rem 0 2rem 0;
    }
    
    .brand-title {
        font-size: 3.8rem;
        font-weight: 900;
        letter-spacing: -1.5px;
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 30%, #ff0844 70%, #ffb199 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 4px 15px rgba(0, 242, 254, 0.3));
        margin-bottom: 0px;
    }
    
    .brand-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        font-weight: 400;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-top: 5px;
    }
    
    /* Vibrant Sidebar Aesthetic */
    [data-testid="stSidebar"] {
        background-color: #0d091a !important;
        border-right: 1px solid rgba(255, 8, 68, 0.15);
    }
    
    /* Dynamic Cyberpunk Headers */
    .matrix-header {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #ffffff;
        margin: 2.5rem 0 1.2rem 0;
        padding-left: 12px;
        border-left: 5px solid #ff0844;
        text-shadow: 0 0 10px rgba(2ff, 8, 68, 0.4);
    }
    
    .matrix-header-cyan {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff;
        margin: 2.5rem 0 1.2rem 0;
        padding-left: 12px;
        border-left: 5px solid #00f2fe;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.4);
    }

    /* Cinematic Movie Card Styling */
    .neon-card {
        background: rgba(20, 15, 38, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 16px;
        padding: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(8px);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .neon-card:hover {
        transform: translateY(-8px) scale(1.02);
        background: rgba(32, 22, 61, 0.8);
        border-color: #00f2fe;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.4), inset 0 0 10px rgba(0, 242, 254, 0.1);
    }
    
    .neon-card img {
        border-radius: 12px;
        width: 100%;
        transition: transform 0.3s;
    }
    
    .neon-card-title {
        font-size: 1rem;
        font-weight: 700;
        color: #ffffff;
        margin-top: 10px;
        padding: 0 4px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Premium Profile Box Block Container */
    .profile-glow-box {
        background: linear-gradient(145deg, rgba(23, 17, 46, 0.85) 0%, rgba(13, 9, 26, 0.95) 100%);
        border: 1px solid rgba(139, 92, 246, 0.2);
        box-shadow: 0 0 40px rgba(139, 92, 246, 0.15);
        border-radius: 24px;
        padding: 35px;
        backdrop-filter: blur(14px);
    }
    
    /* Glowing Micro Badge Tokens */
    .badge-neon-pink {
        background: rgba(255, 8, 68, 0.12);
        color: #ff416c;
        border: 1px solid rgba(255, 8, 68, 0.3);
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.88rem;
        font-weight: 700;
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 10px;
        box-shadow: 0 0 10px rgba(255, 8, 68, 0.1);
    }
    
    .badge-neon-cyan {
        background: rgba(0, 242, 254, 0.12);
        color: #00f2fe;
        border: 1px solid rgba(0, 242, 254, 0.3);
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.88rem;
        font-weight: 700;
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 10px;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.1);
    }
    
    /* Form Input Element Accent Overrides */
    div[data-baseweb="input"] {
        background-color: rgba(15, 10, 28, 0.8) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #00f2fe !important;
        box-shadow: 0 0 12px rgba(0, 242, 254, 0.3) !important;
    }
    
    /* Native Button Transitions Overrides */
    div.stButton > button {
        background: linear-gradient(90deg, rgba(20, 15, 38, 0.8), rgba(32, 22, 61, 0.8)) !important;
        color: #ffffff !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #ff0844 0%, #ffb199 100%) !important;
        border-color: #ff0844 !important;
        box-shadow: 0 0 15px rgba(255, 8, 68, 0.5) !important;
        color: #ffffff !important;
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =============================
# STATE AUTOMATION PIPELINE
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except ValueError:
        pass

def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()

def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()

# =============================
# CALL API HELPERS
# =============================
@st.cache_data(ttl=60)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}"
        return r.json(), None
    except Exception as e:
        return None, f"Network lost: {e}"

def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movie listings encountered inside this dimension matrix.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols, gap="large")
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                poster_src = poster if poster else "https://placehold.co/500x750/100f26/4facfe?text=Cover+Unavailable"
                
                # Squeezing elements inside structural Neon Card layouts
                st.markdown(
                    f"""
                    <div class="neon-card">
                        <img src="{poster_src}" alt="{title}">
                        <div class="neon-card-title">{title}</div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                if st.button("Unlock Details ⚡", key=f"{key_prefix}_{tmdb_id}_{idx}"):
                    if tmdb_id:
                        goto_details(tmdb_id)

def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append({
                "tmdb_id": tmdb["tmdb_id"],
                "title": tmdb.get("title") or x.get("title") or "Untitled",
                "poster_url": tmdb.get("poster_url"),
            })
    return cards

def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()
    raw_items = []

    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if title and tmdb_id:
                raw_items.append({
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                })
    elif isinstance(data, list):
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if title and tmdb_id:
                raw_items.append({
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                })
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards

# =============================
# PREMIUM SIDEBAR PANEL
# =============================
with st.sidebar:
    st.markdown("<h2 style='color: #ffffff; text-shadow: 0 0 10px rgba(139,92,246,0.4);'>🔮 CONTROLS</h2>", unsafe_allow_html=True)
    if st.button("🏠 Primary Dashboard Hub"):
        goto_home()

    st.markdown("<br><hr style='border-color: rgba(139, 92, 246, 0.2);'><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00f2fe;'>🍿 FILTER PIPELINE</h3>", unsafe_allow_html=True)
    
    home_category = st.selectbox(
        "Active Stream Filter",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        format_func=lambda x: f"✨ {x.replace('_', ' ').title()}",
        index=0,
    )
    grid_cols = st.slider("Dynamic Resolution Width (Columns)", 4, 8, 6)

# =============================
# MAIN INTERFACE HEADER ENGINE
# =============================
st.markdown(
    """
    <div class="brand-container">
        <h1 class="brand-title">CINEVERSE ULTRA</h1>
        <div class="brand-subtitle">Vector Alignment Neural Recommendation Framework</div>
    </div>
    """, 
    unsafe_allow_html=True
)

# ==========================================================
# VIEW: HOME DASHBOARD
# ==========================================================
if st.session_state.view == "home":
    typed = st.text_input(
        "🔎 Real-time Search Matrix Entry", 
        placeholder="Input movie title parameters... (e.g. Blade Runner, Interstellar, Dune)"
    )

    # ACTIVE SEARCH MATRIX ACTIONS
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Provide at least 2 tracking variables to trigger the algorithm.")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search framework indexing fault: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

                if suggestions:
                    labels = ["-- Choose exact index signature target --"] + [s[0] for s in suggestions]
                    selected = st.selectbox("🎯 Neural Array Match Array Mapping:", labels, index=0)

                    if selected != "-- Choose exact index signature target --":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])

                st.markdown('<div class="matrix-header-cyan">Identified Cluster Targets Matrix</div>', unsafe_allow_html=True)
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    # CORE BASING FEED CARDS
    category_title = home_category.replace("_"," ").title()
    st.markdown(f'<div class="matrix-header">Trending Stream Feed: {category_title}</div>', unsafe_allow_html=True)

    home_cards, err = api_get_json("/home", params={"category": home_category, "limit": 24})
    if err or not home_cards:
        st.error(f"Failed to fetch content block: {err or 'Unknown mapping break'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")

# ==========================================================
# VIEW: DETAILS MATRICES
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("Identity pointer tracking sequence interrupted.")
        if st.button("← Return Safely To Launch Base"):
            goto_home()
        st.stop()

    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Failed loading database target schema information: {err}")
        st.stop()

    # Split Detail Canvas Structure
    left, right = st.columns([1, 2.2], gap="large")

    with left:
        if data.get("poster_url"):
            st.markdown(f'<div class="neon-card" style="box-shadow: 0 0 30px rgba(139,92,246,0.3);"><img src="{data["poster_url"]}"></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="neon-card" style="padding: 100px 0;">🖼️ Asset Poster Cache Corrupted</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="profile-glow-box">', unsafe_allow_html=True)
        st.markdown(f"<h1 style='margin-top:0; font-weight:800; color:#ffffff; font-size: 2.5rem;'>{data.get('title','')}</h1>", unsafe_allow_html=True)
        
        # Micro Accent Elements
        release_year = data.get("release_date", "----")[:4]
        st.markdown(f'<span class="badge-neon-cyan">📅 TIMELINE: {release_year}</span>', unsafe_allow_html=True)
        
        genres_list = data.get("genres", [])
        if genres_list:
            for g in genres_list[:3]:
                st.markdown(f'<span class="badge-neon-pink">✨ {g["name"].upper()}</span>', unsafe_allow_html=True)
        
        st.markdown("<h3 style='color:#00f2fe; margin-top:25px; font-weight:700;'>SYNOPSIS LOG DATA</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#e2e8f0; font-size:1.1rem; line-height:1.7; font-weight: 300;'>{data.get('overview','No textual log description file cached.')}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Dynamic Backdrop Section
    if data.get("backdrop_url"):
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🖼️ Expand Cinematic Immersive Visual Backdrop"):
            st.image(data["backdrop_url"], use_column_width=True)

    # HYBRID ALGORITHM RESULTS SECTION
    title = (data.get("title") or "").strip()
    if title:
        bundle, err2 = api_get_json("/movie/search", params={"query": title, "tfidf_top_n": 12, "genre_limit": 12})

        if not err2 and bundle:
            st.markdown('<div class="matrix-header">🔎 Similiar Movies (TF-IDF)</div>', unsafe_allow_html=True)
            poster_grid(to_cards_from_tfidf_items(bundle.get("tfidf_recommendations")), cols=grid_cols, key_prefix="details_tfidf")

            st.markdown('<div class="matrix-header-cyan">🎭 GENRE AFFINITY SIGNATURE MATCHES</div>', unsafe_allow_html=True)
            poster_grid(bundle.get("genre_recommendations", []), cols=grid_cols, key_prefix="details_genre")
        else:
            # Fallback Pipelines
            genre_only, err3 = api_get_json("/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18})
            if not err3 and genre_only:
                st.markdown('<div class="matrix-header-cyan">🎭 GENRE AFFINITY SIGNATURE MATCHES (FALLBACK Engine)</div>', unsafe_allow_html=True)
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.info("Algorithmic matching structures operating offline.")