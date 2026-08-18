/* =========================================================
   Room Type Predictor — NYC Airbnb
   Handles: API calls, searchable neighbourhood combobox,
   borough accent theming, animated probability readout.
   ========================================================= */

(function () {
  "use strict";

  // ---- Config -------------------------------------------------
  // Point this at wherever your FastAPI app is running.
  const API_BASE = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"
    ? "http://localhost:8000"
    : "http://localhost:8000"; // change to your deployed API URL

  document.getElementById("apiBaseLabel").textContent = API_BASE;

  // ---- Data: boroughs + neighbourhoods (from the trained encoder) ----
  const BOROUGHS = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"];

  const NEIGHBOURHOODS = ["Allerton", "Arden Heights", "Arrochar", "Arverne", "Astoria", "Bath Beach", "Battery Park City", "Bay Ridge", "Bay Terrace", "Bay Terrace, Staten Island", "Baychester", "Bayside", "Bayswater", "Bedford-Stuyvesant", "Belle Harbor", "Bellerose", "Belmont", "Bensonhurst", "Bergen Beach", "Boerum Hill", "Borough Park", "Breezy Point", "Briarwood", "Brighton Beach", "Bronxdale", "Brooklyn Heights", "Brownsville", "Bull's Head", "Bushwick", "Cambria Heights", "Canarsie", "Carroll Gardens", "Castle Hill", "Castleton Corners", "Chelsea", "Chinatown", "City Island", "Civic Center", "Claremont Village", "Clason Point", "Clifton", "Clinton Hill", "Co-op City", "Cobble Hill", "College Point", "Columbia St", "Concord", "Concourse", "Concourse Village", "Coney Island", "Corona", "Crown Heights", "Cypress Hills", "DUMBO", "Ditmars Steinway", "Dongan Hills", "Douglaston", "Downtown Brooklyn", "Dyker Heights", "East Elmhurst", "East Flatbush", "East Harlem", "East Morrisania", "East New York", "East Village", "Eastchester", "Edenwald", "Edgemere", "Elmhurst", "Eltingville", "Emerson Hill", "Far Rockaway", "Fieldston", "Financial District", "Flatbush", "Flatiron District", "Flatlands", "Flushing", "Fordham", "Forest Hills", "Fort Greene", "Fort Hamilton", "Fresh Meadows", "Glendale", "Gowanus", "Gramercy", "Graniteville", "Grant City", "Gravesend", "Great Kills", "Greenpoint", "Greenwich Village", "Grymes Hill", "Harlem", "Hell's Kitchen", "Highbridge", "Hollis", "Holliswood", "Howard Beach", "Howland Hook", "Huguenot", "Hunts Point", "Inwood", "Jackson Heights", "Jamaica", "Jamaica Estates", "Jamaica Hills", "Kensington", "Kew Gardens", "Kew Gardens Hills", "Kingsbridge", "Kips Bay", "Laurelton", "Little Italy", "Little Neck", "Long Island City", "Longwood", "Lower East Side", "Manhattan Beach", "Marble Hill", "Mariners Harbor", "Maspeth", "Melrose", "Middle Village", "Midland Beach", "Midtown", "Midwood", "Mill Basin", "Morningside Heights", "Morris Heights", "Morris Park", "Morrisania", "Mott Haven", "Mount Eden", "Mount Hope", "Murray Hill", "Navy Yard", "Neponsit", "New Brighton", "New Dorp", "New Dorp Beach", "New Springville", "NoHo", "Nolita", "North Riverdale", "Norwood", "Oakwood", "Olinville", "Ozone Park", "Park Slope", "Parkchester", "Pelham Bay", "Pelham Gardens", "Port Morris", "Port Richmond", "Prince's Bay", "Prospect Heights", "Prospect-Lefferts Gardens", "Queens Village", "Randall Manor", "Red Hook", "Rego Park", "Richmond Hill", "Ridgewood", "Riverdale", "Rockaway Beach", "Roosevelt Island", "Rosebank", "Rosedale", "Rossville", "Schuylerville", "Sea Gate", "Sheepshead Bay", "Shore Acres", "Silver Lake", "SoHo", "Soundview", "South Beach", "South Ozone Park", "South Slope", "Springfield Gardens", "Spuyten Duyvil", "St. Albans", "St. George", "Stapleton", "Stuyvesant Town", "Sunnyside", "Sunset Park", "Theater District", "Throgs Neck", "Todt Hill", "Tompkinsville", "Tottenville", "Tremont", "Tribeca", "Two Bridges", "Unionport", "University Heights", "Upper East Side", "Upper West Side", "Van Nest", "Vinegar Hill", "Wakefield", "Washington Heights", "West Brighton", "West Farms", "West Village", "Westchester Square", "Westerleigh", "Whitestone", "Williamsbridge", "Williamsburg", "Willowbrook", "Windsor Terrace", "Woodhaven", "Woodlawn", "Woodside"];

  const BOROUGH_ACCENTS = {
    "Manhattan": { accent: "#FF9800", dim: "rgba(255, 152, 0, 0.16)", line: "rgba(255, 152, 0, 0.4)" },
    "Brooklyn": { accent: "#00BFA5", dim: "rgba(0, 191, 165, 0.16)", line: "rgba(0, 191, 165, 0.4)" },
    "Queens": { accent: "#7C4DFF", dim: "rgba(124, 77, 255, 0.16)", line: "rgba(124, 77, 255, 0.4)" },
    "Bronx": { accent: "#FF6E6E", dim: "rgba(255, 110, 110, 0.16)", line: "rgba(255, 110, 110, 0.4)" },
    "Staten Island": { accent: "#78909C", dim: "rgba(120, 144, 156, 0.16)", line: "rgba(120, 144, 156, 0.4)" }
  };

  const ROOM_TYPE_COLORS = {
    "Entire home/apt": "#00BFA5",
    "Private room": "#FF9800",
    "Shared room": "#7C4DFF"
  };

  // ---- Element refs -------------------------------------------
  const root = document.documentElement;
  const form = document.getElementById("predictForm");
  const boroughSelect = document.getElementById("neighbourhood_group");
  const nbSearch = document.getElementById("neighbourhood_search");
  const nbHidden = document.getElementById("neighbourhood");
  const comboList = document.getElementById("comboList");

  const minNights = document.getElementById("minimum_nights");
  const minNightsVal = document.getElementById("minNightsVal");
  const avail = document.getElementById("availability_365");
  const availVal = document.getElementById("availVal");

  const predictBtn = document.getElementById("predictBtn");
  const formError = document.getElementById("formError");

  const readoutIdle = document.getElementById("readoutIdle");
  const readoutLoading = document.getElementById("readoutLoading");
  const readoutResult = document.getElementById("readoutResult");

  const resultLabel = document.getElementById("resultLabel");
  const resultConfidence = document.getElementById("resultConfidence");
  const probBars = document.getElementById("probBars");
  const metaNeighbourhood = document.getElementById("metaNeighbourhood");
  const metaBorough = document.getElementById("metaBorough");
  const metaPrice = document.getElementById("metaPrice");

  const resetBtn = document.getElementById("resetBtn");
  const fillSampleBtn = document.getElementById("fillSampleBtn");

  const statusDot = document.getElementById("statusDot");
  const statusLabel = document.getElementById("statusLabel");
  const paneEyebrows = document.querySelectorAll(".pane-eyebrow");
  const brandMark = document.getElementById("brandMark");

  // ---- Populate borough select ---------------------------------
  BOROUGHS.forEach((b) => {
    const opt = document.createElement("option");
    opt.value = b;
    opt.textContent = b;
    boroughSelect.appendChild(opt);
  });

  // ---- Theming: swap accent color by borough --------------------
  function applyAccent(borough) {
    const palette = BOROUGH_ACCENTS[borough] || BOROUGH_ACCENTS["Brooklyn"];
    root.style.setProperty("--accent", palette.accent);
    root.style.setProperty("--accent-dim", palette.dim);
    root.style.setProperty("--accent-line", palette.line);
  }

  boroughSelect.addEventListener("change", () => {
    applyAccent(boroughSelect.value);
  });

  // ---- Searchable neighbourhood combobox -------------------------
  let activeIndex = -1;
  let currentMatches = [];

  function renderMatches(query) {
    const q = query.trim().toLowerCase();
    currentMatches = q === ""
      ? NEIGHBOURHOODS.slice(0, 30)
      : NEIGHBOURHOODS.filter((n) => n.toLowerCase().includes(q)).slice(0, 30);

    comboList.innerHTML = "";
    activeIndex = -1;

    if (currentMatches.length === 0) {
      const li = document.createElement("li");
      li.className = "empty";
      li.textContent = "No neighbourhood matches";
      comboList.appendChild(li);
      return;
    }

    currentMatches.forEach((name, i) => {
      const li = document.createElement("li");
      li.setAttribute("role", "option");
      li.dataset.index = i;

      if (q && name.toLowerCase().startsWith(q)) {
        li.innerHTML = `<mark>${name.slice(0, query.length)}</mark>${name.slice(query.length)}`;
      } else {
        li.textContent = name;
      }

      li.addEventListener("mousedown", (e) => {
        e.preventDefault();
        selectNeighbourhood(name);
      });
      comboList.appendChild(li);
    });
  }

  function selectNeighbourhood(name) {
    nbSearch.value = name;
    nbHidden.value = name;
    closeCombo();
    nbSearch.classList.remove("invalid");
  }

  function openCombo() {
    comboList.classList.add("open");
  }
  function closeCombo() {
    comboList.classList.remove("open");
  }

  nbSearch.addEventListener("focus", () => {
    renderMatches(nbSearch.value);
    openCombo();
  });

  nbSearch.addEventListener("input", () => {
    nbHidden.value = ""; // require explicit selection
    renderMatches(nbSearch.value);
    openCombo();
  });

  nbSearch.addEventListener("keydown", (e) => {
    const items = comboList.querySelectorAll("li:not(.empty)");
    if (e.key === "ArrowDown") {
      e.preventDefault();
      activeIndex = Math.min(activeIndex + 1, items.length - 1);
      updateActiveItem(items);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      activeIndex = Math.max(activeIndex - 1, 0);
      updateActiveItem(items);
    } else if (e.key === "Enter") {
      if (activeIndex >= 0 && currentMatches[activeIndex]) {
        e.preventDefault();
        selectNeighbourhood(currentMatches[activeIndex]);
      }
    } else if (e.key === "Escape") {
      closeCombo();
    }
  });

  function updateActiveItem(items) {
    items.forEach((it) => it.classList.remove("active"));
    if (items[activeIndex]) {
      items[activeIndex].classList.add("active");
      items[activeIndex].scrollIntoView({ block: "nearest" });
    }
  }

  document.addEventListener("click", (e) => {
    if (!document.getElementById("comboWrap").contains(e.target)) {
      closeCombo();
    }
  });

  // ---- Sliders: live value readout --------------------------------
  minNights.addEventListener("input", () => { minNightsVal.textContent = minNights.value; });
  avail.addEventListener("input", () => { availVal.textContent = avail.value; });

  // ---- Sample data fill ---------------------------------------------
  fillSampleBtn.addEventListener("click", () => {
    boroughSelect.value = "Brooklyn";
    applyAccent("Brooklyn");
    selectNeighbourhood("Williamsburg");
    document.getElementById("latitude").value = "40.71455";
    document.getElementById("longitude").value = "-73.95765";
    document.getElementById("price").value = "125";
    minNights.value = 3; minNightsVal.textContent = "3";
    avail.value = 210; availVal.textContent = "210";
    document.getElementById("number_of_reviews").value = "48";
    document.getElementById("reviews_per_month").value = "1.85";
    document.getElementById("calculated_host_listings_count").value = "2";
    formError.textContent = "";
  });

  // ---- API status check -----------------------------------------
  async function checkApiStatus() {
    try {
      const res = await fetch(`${API_BASE}/`, { method: "GET" });
      if (res.ok) {
        statusDot.className = "status-dot ok";
        statusLabel.textContent = "API connected";
      } else {
        throw new Error("bad status");
      }
    } catch (err) {
      statusDot.className = "status-dot err";
      statusLabel.textContent = "API unreachable";
    }
  }
  checkApiStatus();

  // ---- Form submit → predict --------------------------------------
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    formError.textContent = "";

    if (!nbHidden.value) {
      formError.textContent = "Please select a neighbourhood from the list.";
      nbSearch.focus();
      return;
    }
    if (!boroughSelect.value) {
      formError.textContent = "Please select a borough.";
      boroughSelect.focus();
      return;
    }

    const payload = {
      latitude: parseFloat(document.getElementById("latitude").value),
      longitude: parseFloat(document.getElementById("longitude").value),
      price: parseFloat(document.getElementById("price").value),
      minimum_nights: parseInt(minNights.value, 10),
      number_of_reviews: parseInt(document.getElementById("number_of_reviews").value, 10),
      reviews_per_month: parseFloat(document.getElementById("reviews_per_month").value),
      calculated_host_listings_count: parseInt(document.getElementById("calculated_host_listings_count").value, 10),
      availability_365: parseInt(avail.value, 10),
      neighbourhood_group: boroughSelect.value,
      neighbourhood: nbHidden.value
    };

    for (const [key, val] of Object.entries(payload)) {
      if (typeof val === "number" && Number.isNaN(val)) {
        formError.textContent = `Please fill a valid value for "${key.replace(/_/g, " ")}".`;
        return;
      }
    }

    showLoading();
    setBtnLoading(true);

    try {
      const res = await fetch(`${API_BASE}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`API returned ${res.status}: ${text}`);
      }

      const data = await res.json();
      renderResult(data, payload);
    } catch (err) {
      showIdle();
      formError.textContent = `Prediction failed — ${err.message}`;
    } finally {
      setBtnLoading(false);
    }
  });

  function setBtnLoading(isLoading) {
    predictBtn.classList.toggle("loading", isLoading);
    predictBtn.disabled = isLoading;
  }

  function showIdle() {
    readoutIdle.hidden = false;
    readoutLoading.hidden = true;
    readoutResult.hidden = true;
  }

  function showLoading() {
    readoutIdle.hidden = true;
    readoutLoading.hidden = false;
    readoutResult.hidden = true;
  }

  function showResultView() {
    readoutIdle.hidden = true;
    readoutLoading.hidden = true;
    readoutResult.hidden = false;
  }

  // ---- Render prediction result -------------------------------------
  function renderResult(data, payload) {
    const predicted = data.Predicted_Room_Type;
    const probs = data.Probability; // array aligned to model.classes_ order

    // model.classes_ order confirmed as:
    const CLASS_ORDER = ["Entire home/apt", "Private room", "Shared room"];

    const rows = CLASS_ORDER.map((name, i) => ({
      name,
      pct: (probs[i] ?? 0) * 100
    })).sort((a, b) => b.pct - a.pct);

    const topPct = rows[0].pct;

    showResultView();

    resultLabel.textContent = predicted;
    resultLabel.style.color = ROOM_TYPE_COLORS[predicted] || "var(--accent)";
    resultConfidence.textContent = `${topPct.toFixed(1)}% confidence`;

    metaNeighbourhood.textContent = payload.neighbourhood;
    metaBorough.textContent = payload.neighbourhood_group;
    metaPrice.textContent = `$${payload.price}`;

    probBars.innerHTML = "";
    rows.forEach((row, idx) => {
      const isWinner = row.name === predicted;
      const wrap = document.createElement("div");
      wrap.className = "prob-row" + (isWinner ? " winner" : "");

      wrap.innerHTML = `
        <div class="prob-row-top">
          <span class="prob-row-name">${row.name}</span>
          <span class="prob-row-pct">${row.pct.toFixed(1)}%</span>
        </div>
        <div class="prob-track">
          <div class="prob-fill" style="background:${ROOM_TYPE_COLORS[row.name]}"></div>
        </div>
      `;
      probBars.appendChild(wrap);

      // animate width after insertion, staggered
      const fill = wrap.querySelector(".prob-fill");
      requestAnimationFrame(() => {
        setTimeout(() => {
          fill.style.width = row.pct + "%";
        }, 80 + idx * 120);
      });
    });
  }

  resetBtn.addEventListener("click", () => {
    showIdle();
    formError.textContent = "";
  });

  // ---- init ----------------------------------------------------
  applyAccent("Brooklyn");
})();