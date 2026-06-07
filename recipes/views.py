from django.views.generic import TemplateView


class RecipeListView(TemplateView):
    template_name = "recipes/recipe_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["recipes"] = [
            {
                "title": "Simple Heritage Tomato Salad",
                "tagline": "A fresh no-cook salad for ripe mixed tomatoes.",
                "time": "10 minutes",
                "difficulty": "Easy",
                "description": (
                    "Slice mixed heritage tomatoes and serve with olive oil, "
                    "sea salt, basil and a splash of vinegar. Best with colourful "
                    "varieties from the Seed Library."
                ),
            },
            {
                "title": "Roasted Tomato Sauce",
                "tagline": "A simple sauce for pasta, pizza or freezing.",
                "time": "45 minutes",
                "difficulty": "Easy",
                "description": (
                    "Roast tomatoes with garlic, herbs and olive oil, then blend "
                    "or crush into a rich seasonal sauce. Useful for tomato gluts."
                ),
            },
            {
                "title": "Green Tomato Chutney",
                "tagline": "A useful preserve for end-of-season green tomatoes.",
                "time": "1–2 hours",
                "difficulty": "Medium",
                "description": (
                    "A traditional chutney idea for unripe tomatoes, onions, vinegar, "
                    "sugar and warming spices. Ideal for reducing autumn waste."
                ),
            },
        ]

        return context