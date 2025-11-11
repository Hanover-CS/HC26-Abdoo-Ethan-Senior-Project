# Practice Exercises

These exercises help you explore Django beyond what the tutorial provides.

---

## Exercise 1 — Add a New Page

1. In `members/views.py`, create a new view called `contact`:

```python
def contact(request):
    return HttpResponse("Contact page for PantherConnect!")
