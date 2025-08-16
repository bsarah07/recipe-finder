document.getElementById("cookBtn").addEventListener("click", async () => {
    const ingredients = document.getElementById("ingredients").value.trim();

    if (!ingredients) {
        alert("Please enter some ingredients!");
        return;
    }

    try {
        const response = await fetch("/get_recipe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ ingredients })
        });

        const data = await response.json();

        // Update the recipe section
        document.getElementById("recipe-img").src = data.image;
        document.getElementById("recipe-title").textContent = data.title;
        document.getElementById("recipe-servings").textContent = data.servings;
        document.getElementById("recipe-time").textContent = data.time;
        document.getElementById("recipe-description").textContent = data.description;

        const stepsList = document.getElementById("recipe-steps");
        stepsList.innerHTML = "";
        data.steps.forEach(step => {
            const li = document.createElement("li");
            li.textContent = step;
            stepsList.appendChild(li);
        });

        document.getElementById("recipe").classList.remove("hidden");

    } catch (error) {
        console.error("Error fetching recipe:", error);
    }
});
