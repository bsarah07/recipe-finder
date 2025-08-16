from flask import Flask, render_template, request, jsonify
import cohere
import json
app = Flask(__name__)
COHERE_API_KEY = "9VFgevDjm7GuXZLPdDHPariuQVUpjZHeYpB8F4oG"
json_recipe = {}
def generate_paragraph(ingredients):
    global json_recipe
    # Commented out in order not to waste API tokens
    co = cohere.Client(COHERE_API_KEY)
    response = co.generate(
        prompt=f"Generate one recipe that requires ONLY the following ingredients: {ingredients}. Your response should ONLY be a dictionary with these keys: - recipe_img - recipe_title - serving_size - cooking_time - description - steps. You fill in the key values with the information. DO NOT ADD IN ANY OTHER PHRASE BESIDES THE DICTIONARY. ABSOLUTELY Leave no trailing comma that si not necessary to the succesful turning to a json file. MAKE SURE IMAGE URL ACTUALLY WORKS. ",
        max_tokens=600
    )

    recipe = response.generations[0].text.strip()
    print(recipe)
    json_recipe = json.loads(recipe)

    return json_recipe


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_recipe", methods=["POST"])
def get_recipe():
    data = request.get_json()
    ingredients = data.get("ingredients", "")
    print(ingredients)


    generate_paragraph(ingredients=ingredients)
    recipe = {
        "title": json_recipe["recipe_title"],
        "servings": json_recipe["serving_size"],
        "time": json_recipe["cooking_time"],
        "description": json_recipe["description"],
        "image": json_recipe["recipe_img"],
        "steps": json_recipe["steps"]


    }

    return jsonify(recipe)

if __name__ == "__main__":
    app.run(debug=True)
