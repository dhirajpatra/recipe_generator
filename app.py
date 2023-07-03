from flask import Flask, render_template, request, jsonify
import openai
# import gpt_2_simple as gpt2

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "YOUR_OPENAI_API_KEY"

# Available ingredients, kitchen tools, and chef modes
ingredients = [
    "Apple",
    "Avocado",
    "Banana",
    "Basil",
    "Beef",
    "Beer",
    "Bell peppers",
    "Bread",
    "Broccoli",
    "Butter",
    "Cabbage",
    "Carrots",
    "Celery",
    "Cheese",
    "Chicken",
    "Chili",
    "Chocolate",
    "Cloves",
    "Coffee",
    "Coriander",
    "Corn",
    "Crab",
    "Cumin",
    "Eggplant",
    "Eggs",
    "Fish",
    "Flour",
    "Garlic",
    "Ginger",
    "Grapes",
    "Honey",
    "Lemon",
    "Lettuce",
    "Lime",
    "Lobster",
    "Milk",
    "Mint",
    "Mushrooms",
    "Mussels",
    "Nutmeg",
    "Nuts",
    "Octopus",
    "Olive oil",
    "Onion",
    "Oats",
    "Oregano",
    "Palm oil",
    "Parsley",
    "Peanut butter",
    "Peppers",
    "Pineapple",
    "Pizza",
    "Potatoes",
    "Rice",
    "Rosemary",
    "Salt",
    "Sesame oil",
    "Sesame seeds",
    "Shrimp",
    "Soya sauce",
    "Spinach",
    "Squid",
    "Sugar",
    "Tea",
    "Thyme",
    "Tomato",
    "Vanilla",
    "Vinegar",
    "Wine",
]
kitchen_tools = [
    "Stove Top",
    "Oven",
    "Microwave",
    "Air Fryer",
    "Sous Vide Machine",
    "Blender",
    "Food Processor",
    "BBQ",
    "Slow Cooker",
    "Pressure Cooker",
]
chef_modes = ["Gourmate mode", "All in one"]


@app.route("/")
def index():
    return render_template(
        "index.html",
        ingredients=ingredients,
        kitchen_tools=kitchen_tools,
        chef_modes=chef_modes,
    )


@app.route("/generate_recipe", methods=["POST"])
def generate_recipe():
    user_ingredients = request.form.getlist("ingredients[]")
    user_tools = request.form.getlist("tools[]")
    user_time = request.form["time"]
    user_chef_mode = request.form["chef_mode"]

    # Construct the prompt for recipe generation
    prompt = f"What can I cook with {', '.join(user_ingredients)} using {', '.join(user_tools)} in under {user_time} minutes? I am a {user_chef_mode} chef."

    # Generate the recipe using OpenAI language model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.8,
        n=1,
        stop=None,
        temperature=0.8,
        n=1,
        stop=None,
    )

    # Extract the generated recipe from the response
    recipe = response.choices[0].text.strip()

    # # Generate the recipe using GPT-2 model
    # recipe = gpt2.generate(
    #     sess, prefix=prompt, length=200, temperature=0.7, return_as_list=True
    # )[0]

    # Return the generated recipe as a JSON response
    return jsonify({"recipe": recipe})


if __name__ == "__main__":
    app.run(debug=True)
