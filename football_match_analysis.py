import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

# ==========================================
# FOOTBALL MATCH & PLAYER PERFORMANCE ANALYZER
# DAA MINI PROJECT - PYTHON
# ==========================================

st.set_page_config(
    page_title="Football Performance Analyzer",
    page_icon="⚽",
    layout="wide"
)

# Apply Clean Dark Theme for Matplotlib Charts
plt.style.use('dark_background')

# ==========================================
# 1. PLAYER DATA
# ==========================================

player_data = [
    ["Erling Haaland", "Man City", "Forward", 22, 18, 61, 84.2, 8.1],
    ["Kevin De Bruyne", "Man City", "Midfielder", 8, 14, 49, 89.4, 8.0],
    ["Phil Foden", "Man City", "Midfielder", 11, 7, 52, 87.6, 7.8],
    ["Bukayo Saka", "Arsenal", "Forward", 14, 9, 57, 82.8, 8.0],
    ["Martin Odegaard", "Arsenal", "Midfielder", 7, 8, 36, 89.1, 7.7],
    ["Declan Rice", "Arsenal", "Midfielder", 5, 6, 21, 91.2, 7.5],
    ["Mohamed Salah", "Liverpool", "Forward", 16, 9, 63, 79.8, 8.2],
    ["Virgil van Dijk", "Liverpool", "Defender", 2, 1, 8, 92.4, 7.4],
    ["Son Heung-min", "Tottenham", "Forward", 12, 5, 42, 84.1, 7.8],
    ["Cole Palmer", "Chelsea", "Forward", 15, 8, 48, 82.2, 8.1],
    ["Bruno Fernandes", "Man United", "Midfielder", 6, 6, 39, 79.6, 7.3],
    ["Marcus Rashford", "Man United", "Forward", 5, 3, 31, 78.4, 6.9],
    ["Ollie Watkins", "Aston Villa", "Forward", 14, 8, 47, 76.9, 7.8],
    ["Alexander Isak", "Newcastle", "Forward", 13, 2, 39, 81.4, 7.6],
    ["Jarrod Bowen", "West Ham", "Forward", 10, 3, 34, 80.3, 7.3],
    ["Dominic Solanke", "Bournemouth", "Forward", 12, 1, 37, 73.8, 7.4],
]

players = pd.DataFrame(
    player_data,
    columns=[
        "Player", "Team", "Position", "Goals",
        "Assists", "Shots", "Pass Accuracy", "Rating"
    ]
)

# Illustrative project scoring formula
players["Performance Score"] = (
    players["Goals"] * 4
    + players["Assists"] * 3
    + players["Pass Accuracy"] * 0.08
    + players["Rating"] * 2
).round(2)

# ==========================================
# 2. MATCH DATA
# ==========================================

match_data = [
    ["Manchester City", "Arsenal", 2, 1, 58, 8, 5],
    ["Liverpool", "Chelsea", 3, 1, 62, 9, 4],
    ["Tottenham", "Manchester City", 0, 2, 43, 3, 7],
    ["Arsenal", "Liverpool", 1, 1, 53, 5, 5],
    ["Chelsea", "Manchester United", 2, 1, 57, 7, 4],
    ["Aston Villa", "Arsenal", 1, 2, 47, 4, 6],
    ["Manchester United", "Liverpool", 1, 3, 45, 4, 8],
    ["Newcastle", "Chelsea", 2, 2, 51, 6, 5],
]

matches = pd.DataFrame(
    match_data,
    columns=[
        "Home Team", "Away Team", "Home Goals",
        "Away Goals", "Home Possession",
        "Home Shots on Target", "Away Shots on Target"
    ]
)

# ==========================================
# 3. DAA ALGORITHMS
# ==========================================

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ==========================================
# 4. PROFESSIONAL DASHBOARD STYLING (CSS)
# ==========================================

st.markdown("""
<style>
/* Main Background */
.stApp {
    background-color: #0b132b;
    color: #ffffff !important;
}

/* Force all Headings, Titles and Text to White for High Visibility */
h1, h2, h3, h4, h5, h6, 
.stTitle, .stHeader, p, span, label, div {
    color: #ffffff !important;
}

/* Specific override for main title to ensure high brightness */
h1 {
    color: #ffffff !important;
    font-weight: 700;
}

h2, h3 {
    color: #ffffff !important;
    font-weight: 600;
}

/* Metric Cards Styling */
[data-testid="stMetric"] {
    background-color: #1c2541 !important;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #3a506b;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

[data-testid="stMetricLabel"] {
    color: #ffffff !important;
    font-size: 15px !important;
}

[data-testid="stMetricValue"] {
    color: #4cc9f0 !important;
    font-size: 28px !important;
    font-weight: bold;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: #1c2541 !important;
    border-right: 1px solid #3a506b;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

st.title("⚽ Football Match & Player Performance Analyzer")

st.write(
    "A Python-based DAA mini project for player statistics, "
    "match comparison, ranking and algorithm analysis."
)

st.sidebar.title("⚽ Navigation")

page = st.sidebar.radio(
    "Choose a section",
    [
        "Dashboard",
        "Player Analysis",
        "Match Comparison",
        "DAA Algorithm Lab",
        "About Project"
    ]
)

# ==========================================
# 5. DASHBOARD
# ==========================================

if page == "Dashboard":

    st.header("Season Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Players", len(players))
    c2.metric("Teams", players["Team"].nunique())
    c3.metric("Total Goals", int(players["Goals"].sum()))
    c4.metric(
        "Average Rating",
        round(players["Rating"].mean(), 2)
    )

    st.subheader("Top 10 Players")

    top_players = players.sort_values(
        "Performance Score", ascending=False
    ).head(10)

    fig, ax = plt.subplots(figsize=(10, 5), facecolor='#0b132b')
    ax.set_facecolor('#1c2541')

    ax.barh(
        top_players["Player"].iloc[::-1],
        top_players["Performance Score"].iloc[::-1],
        color='#4cc9f0'
    )

    ax.set_xlabel("Performance Score", color='#ffffff')
    ax.set_title("Top Players Ranking", color='#ffffff', fontsize=14, fontweight='bold')
    ax.tick_params(colors='#ffffff')
    ax.grid(axis="x", alpha=0.2, color='#8d99ae')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Goals by Team")

    team_goals = (
        players.groupby("Team")["Goals"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 4), facecolor='#0b132b')
    ax.set_facecolor('#1c2541')

    ax.bar(team_goals.index, team_goals.values, color='#4361ee')
    ax.set_ylabel("Goals", color='#ffffff')
    ax.tick_params(axis="x", rotation=35, colors='#ffffff')
    ax.tick_params(axis="y", colors='#ffffff')
    ax.grid(axis="y", alpha=0.2, color='#8d99ae')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Top Performers Table")

    st.dataframe(
        top_players,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "The included statistics are illustrative demo data, "
        "not verified official season records."
    )

# ==========================================
# 6. PLAYER ANALYSIS
# ==========================================

elif page == "Player Analysis":

    st.header("Player Performance Analysis")

    team_list = ["All Teams"] + sorted(
        players["Team"].unique().tolist()
    )

    selected_team = st.selectbox("Select Team", team_list)

    filtered = players.copy()

    if selected_team != "All Teams":
        filtered = filtered[
            filtered["Team"] == selected_team
        ]

    search = st.text_input("Search Player by Name")

    if search:
        filtered = filtered[
            filtered["Player"].str.contains(
                search, case=False, na=False
            )
        ]

    sort_option = st.selectbox(
        "Rank Players By",
        [
            "Performance Score",
            "Goals",
            "Assists",
            "Rating",
            "Pass Accuracy"
        ]
    )

    filtered = filtered.sort_values(
        sort_option, ascending=False
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

    if not filtered.empty:

        selected_player = st.selectbox(
            "View Player Profile",
            filtered["Player"].tolist()
        )

        p = filtered[
            filtered["Player"] == selected_player
        ].iloc[0]

        st.subheader(selected_player)

        a, b, c, d = st.columns(4)

        a.metric("Goals", int(p["Goals"]))
        b.metric("Assists", int(p["Assists"]))
        c.metric("Rating", p["Rating"])
        d.metric("Performance Score", p["Performance Score"])

        stats = ["Goals", "Assists", "Shots"]

        fig, ax = plt.subplots(figsize=(7, 4), facecolor='#0b132b')
        ax.set_facecolor('#1c2541')

        ax.bar(stats, [p[x] for x in stats], color='#f72585')
        ax.set_title(f"{selected_player} - Statistics", color='#ffffff', fontweight='bold')
        ax.tick_params(colors='#ffffff')
        ax.grid(axis="y", alpha=0.2, color='#8d99ae')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    st.download_button(
        "Download Player Data CSV",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="player_analysis.csv",
        mime="text/csv"
    )

# ==========================================
# 7. MATCH COMPARISON
# ==========================================

elif page == "Match Comparison":

    st.header("Football Match Comparison")

    match_labels = [
        f"{row['Home Team']} vs {row['Away Team']}"
        for _, row in matches.iterrows()
    ]

    selected_match = st.selectbox(
        "Select Match", match_labels
    )

    index = match_labels.index(selected_match)
    match = matches.iloc[index]

    home = match["Home Team"]
    away = match["Away Team"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"🏠 {home}")
        st.metric("Goals", int(match["Home Goals"]))
        st.metric(
            "Possession",
            f"{match['Home Possession']}%"
        )
        st.metric(
            "Shots on Target",
            int(match["Home Shots on Target"])
        )

    with col2:
        st.subheader(f"✈️ {away}")
        st.metric("Goals", int(match["Away Goals"]))
        st.metric(
            "Possession (estimated)",
            f"{100 - match['Home Possession']}%"
        )
        st.metric(
            "Shots on Target",
            int(match["Away Shots on Target"])
        )

    st.subheader("Team Statistics Comparison")

    categories = ["Goals", "Shots on Target"]

    home_values = [
        match["Home Goals"],
        match["Home Shots on Target"]
    ]

    away_values = [
        match["Away Goals"],
        match["Away Shots on Target"]
    ]

    fig, ax = plt.subplots(figsize=(8, 4), facecolor='#0b132b')
    ax.set_facecolor('#1c2541')

    x = list(range(len(categories)))
    width = 0.35

    ax.bar(
        [i - width / 2 for i in x],
        home_values,
        width,
        label=home,
        color='#4cc9f0'
    )

    ax.bar(
        [i + width / 2 for i in x],
        away_values,
        width,
        label=away,
        color='#f72585'
    )

    ax.set_xticks(x)
    ax.set_xticklabels(categories, color='#ffffff')
    ax.tick_params(colors='#ffffff')
    ax.legend(facecolor='#1c2541', edgecolor='#3a506b', labelcolor='#ffffff')
    ax.grid(axis="y", alpha=0.2, color='#8d99ae')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.caption(
        "Match records are illustrative examples for the project."
    )

# ==========================================
# 8. DAA ALGORITHM LAB
# ==========================================

elif page == "DAA Algorithm Lab":

    st.header("DAA Algorithm Performance Lab")

    st.write(
        "Compare sorting and searching algorithms "
        "using execution time and complexity."
    )

    st.subheader("1. Merge Sort vs Quick Sort")

    n = st.slider(
        "Number of elements",
        min_value=100,
        max_value=3000,
        value=1000,
        step=100
    )

    random.seed(42)

    numbers = [
        random.randint(0, 100000)
        for _ in range(n)
    ]

    if st.button("Run Sorting Comparison"):

        start = time.perf_counter()
        merge_result = merge_sort(numbers)
        merge_time = time.perf_counter() - start

        start = time.perf_counter()
        quick_result = quick_sort(numbers)
        quick_time = time.perf_counter() - start

        st.success(
            f"Both algorithms produce the same sorted result: "
            f"{merge_result == quick_result}"
        )

        result_df = pd.DataFrame({
            "Algorithm": ["Merge Sort", "Quick Sort"],
            "Execution Time (seconds)": [
                merge_time, quick_time
            ],
            "Time Complexity": [
                "O(n log n)",
                "Average O(n log n), worst O(n²)"
            ]
        })

        st.dataframe(
            result_df,
            use_container_width=True,
            hide_index=True
        )

        fig, ax = plt.subplots(figsize=(7, 4), facecolor='#0b132b')
        ax.set_facecolor('#1c2541')

        ax.bar(
            result_df["Algorithm"],
            result_df["Execution Time (seconds)"],
            color=['#4cc9f0', '#7209b7']
        )

        ax.set_ylabel("Seconds", color='#ffffff')
        ax.set_title("Sorting Algorithm Benchmark", color='#ffffff', fontweight='bold')
        ax.tick_params(colors='#ffffff')
        ax.grid(axis="y", alpha=0.2, color='#8d99ae')

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    st.subheader("2. Linear Search vs Binary Search")

    sorted_numbers = list(range(100000))

    target = st.number_input(
        "Enter number to search",
        min_value=0,
        max_value=99999,
        value=50000
    )

    if st.button("Run Searching Comparison"):

        start = time.perf_counter()
        linear_index = linear_search(
            sorted_numbers, int(target)
        )
        linear_time = time.perf_counter() - start

        start = time.perf_counter()
        binary_index = binary_search(
            sorted_numbers, int(target)
        )
        binary_time = time.perf_counter() - start

        search_results = pd.DataFrame({
            "Algorithm": [
                "Linear Search",
                "Binary Search"
            ],
            "Index Found": [
                linear_index,
                binary_index
            ],
            "Execution Time (seconds)": [
                linear_time,
                binary_time
            ],
            "Time Complexity": [
                "O(n)",
                "O(log n)"
            ]
        })

        st.dataframe(
            search_results,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            "Binary Search requires sorted data. "
            "Very small timing differences are hardware-dependent."
        )

    st.subheader("Algorithm Complexity Table")

    complexity = pd.DataFrame({
        "Algorithm": [
            "Linear Search",
            "Binary Search",
            "Merge Sort",
            "Quick Sort"
        ],
        "Best Case": [
            "O(1)", "O(1)", "O(n log n)", "O(n log n)"
        ],
        "Average Case": [
            "O(n)", "O(log n)", "O(n log n)", "O(n log n)"
        ],
        "Worst Case": [
            "O(n)", "O(log n)", "O(n log n)", "O(n²)"
        ]
    })

    st.dataframe(
        complexity,
        use_container_width=True,
        hide_index=True
    )

# ==========================================
# 9. ABOUT PROJECT
# ==========================================

elif page == "About Project":

    st.header("About the Project")

    st.write("""
    **Project Name:** Football Match & Player Performance Analyzer

    **Programming Language:** Python

    **Libraries:** Streamlit, Pandas, Matplotlib

    **Subject:** Design and Analysis of Algorithms (DAA)

    **Main Objectives:**
    - Analyze football player statistics.
    - Rank players using a performance score.
    - Compare football match statistics.
    - Implement searching and sorting algorithms.
    - Measure algorithm execution time.
    - Study best, average and worst-case complexity.

    **Algorithms Implemented:**
    1. Merge Sort
    2. Quick Sort
    3. Linear Search
    4. Binary Search

    **Performance Score Formula:**

    Score = (Goals × 4) + (Assists × 3)
    + (Pass Accuracy × 0.08) + (Rating × 2)

    This is an illustrative score designed for this project,
    not an official football rating.

    **Data Note:** The player and match statistics included here
    are demo values. They should not be presented as verified
    real-world or live football statistics.
    """)

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Football Match & Player Performance Analyzer | "
    "Python DAA Mini Project"
)