# Practice Exercises

These exercises help you explore Django beyond what the tutorial provides.

---

## Exercise 1 — Add a New Page

1. In `members/views.py`, create a new view called `contact`:

```python
def contact(request):
    return HttpResponse("Contact page for PantherConnect!")
```
You should now be able to see a contact page for your app!

## Exercise 2 — Customize Your Index Page

1. Open `members/views.py` and modify the `index` view to return a new message:

```python
def index(request):
    return HttpResponse("Welcome to the updated PantherConnect homepage!")
```

You should now see your updated homepage message!