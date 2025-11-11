# Handling Requests & Views

Django uses **views** to decide what content is returned when a user visits a URL. You can create multiple views in a single app.

---

## Adding a New View

Open `pc/views.py` and add the following below your existing `index` view:

```python
def about(request):
    return HttpResponse("PantherConnect helps connect campus clubs!")
