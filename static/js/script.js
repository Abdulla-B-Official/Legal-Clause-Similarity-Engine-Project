"use strict";

const searchBtn = document.getElementById("searchBtn");
const queryInput = document.getElementById("query");
const topKInput = document.getElementById("topK");
const status = document.getElementById("status");
const results = document.getElementById("results");

searchBtn.addEventListener("click", searchClauses);

async function searchClauses() {
    const query = queryInput.value.trim();
    const top_k = Number(topKInput.value);

    if (!query) {
        status.textContent = "Please enter a legal clause.";
        results.innerHTML = "";
        return;
    }

    status.textContent = "Searching...";
    results.innerHTML = "";

    try {
        const response = await fetch("/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query, top_k })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Search failed.");
        }

        status.textContent = `Found ${data.results.length} similar clauses.`;

        data.results.forEach(result => {
            const card = document.createElement("div");

            card.className = "result";

            card.innerHTML = `
                <div class="result-header">
                    <span>Rank ${result.rank}</span>
                    <span class="similarity">${(result.similarity * 100).toFixed(2)}%</span>
                </div>
                <div class="category">${result.category}</div>
                <p class="clause">${result.clause}</p>
            `;

            results.appendChild(card);
        });

    } catch (error) {
        status.textContent = error.message;
    }
}