from django.conf import settings
from firebase_admin import initialize_app, get_app
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from allauth.account.views import LoginView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


try:
    default_app = get_app()
except:
    cred = credentials.Certificate("serviceaccount.json")
    default_app = initialize_app(cred, {
        'storageBucket': 'bukkateria-app-be22a.appspot.com'
    })

db = firestore.client()
bucket = storage.bucket()

# blobs = bucket.list_blobs(prefix='pictures/')
# for blob in blobs:
#     print(blob.name)


class DashboardLogin(LoginView):
    template_name = "dashboard/login.html"

@login_required
def home(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")

    if request.method == 'POST':
        menu_id = request.POST.get('menu_id', '')
        print("Menu ID: ", menu_id)
        menu = menus_ref.document(menu_id).get().to_dict()
        print("Menu Data: ", menu)
        return render(request, 'dashboard/partials/menu-detail.html', {
            'menu_detail': menu
        })

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())

    ctx['results'] = [item.to_dict() for item in menus_ref.get()]
    return render(request, 'dashboard/home.html', ctx)


@login_required
def menus(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")

    if request.method == 'POST':
        menu_id = request.POST.get('menu_id', '')
        print("Menu ID: ", menu_id)
        menu = menus_ref.document(menu_id).get().to_dict()
        print("Menu Data: ", menu)
        return render(request, 'dashboard/partials/menu-detail.html', {
            'menu_detail': menu
        })

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())

    ctx['results'] = [item.to_dict() for item in menus_ref.get()]
    return render(request, 'dashboard/menus.html', ctx)


@login_required
def delete_menu(request):
    if request.method == 'POST':
        menu_id = request.POST.get("menu_id", "")
        menu_ref = db.collection("Menu")
        print("Menu ID: ", menu_id)
        menu_ref.document(menu_id).delete()
        messages.add_message(request, messages.SUCCESS, "Menu Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "menusListChanged"})

    if request.method == 'GET':
        id = request.GET.get('menu_id', '')
        return render(request, "dashboard/partials/delete-menu.html", {
            "menu_id": id,
        })


@login_required
def recipes(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")

    if request.method == 'POST':
        id = request.POST.get('id', '')
        recipe = recipes_ref.document(id).get().to_dict()
        print("Recipe Data: ", recipe)
        return render(request, 'dashboard/partials/recipe-detail.html', {
            'detail': recipe
        })

    results = [item.to_dict() for item in recipes_ref.get()]
    print("Recipes Data: ", results)

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())
    ctx['results'] = results

    return render(request, 'dashboard/recipes.html', ctx)


@login_required
def delete_recipe(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        recipes_ref = db.collection("Recipe")
        recipes_ref.document(id).delete()
        messages.add_message(request, messages.SUCCESS, "Recipe Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "recipesListChanged"})

    if request.method == 'GET':
        id = request.GET.get('id', '')
        return render(request, "dashboard/partials/delete-recipe.html", {
            "id": id,
        })


@login_required
def explore(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")
    explores_ref = db.collection("Explore")

    if request.method == 'POST':
        id = request.POST.get('id', '')
        explore = explores_ref.document(id).get().to_dict()
        print("Explore Data: ", explore)
        return render(request, 'dashboard/partials/explore-detail.html', {
            'detail': explore
        })

    results = [item.to_dict() for item in explores_ref.get()]
    print("Explores Data: ", results)

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())
    ctx['results'] = results

    return render(request, 'dashboard/explores.html', ctx)


@login_required
def delete_explore(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        explores_ref = db.collection("Explore")
        explores_ref.document(id).delete()
        messages.add_message(request, messages.SUCCESS, "Explore Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "exploresListChanged"})

    if request.method == 'GET':
        id = request.GET.get('id', '')
        return render(request, "dashboard/partials/delete-explore.html", {
            "id": id,
        })


@login_required
def users(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")

    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        user_ref = users_ref.document(user_id).get().to_dict()
        print("User Data: ", user_ref)
        return render(request, 'dashboard/partials/user-detail.html', {
            'user_detail': user_ref
        })

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())

    ctx['results'] = [item.to_dict() for item in users_ref.get()]
    return render(request, 'dashboard/users.html', ctx)


@login_required
def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id", "")
        users_ref = db.collection("User")
        print("User ID: ", user_id)
        users_ref.document(user_id).delete()
        messages.add_message(request, messages.SUCCESS, "User Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "usersListChanged"})

    if request.method == 'GET':
        id = request.GET.get('user_id', '')
        return render(request, "dashboard/partials/delete-user.html", {
            "user_id": id,
        })


@login_required
def orders(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")

    if request.method == 'POST':
        id = request.POST.get('id', '')
        order = orders_ref.document(id).get().to_dict()
        print("Order Data: ", order)
        return render(request, 'dashboard/partials/order-detail.html', {
            'detail': order
        })

    results = [item.to_dict() for item in orders_ref.get()]
    print("Orders Data: ", results)

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())
    ctx['results'] = results

    return render(request, 'dashboard/orders.html', ctx)


@login_required
def delete_order(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        orders_ref = db.collection("Order")
        orders_ref.document(id).delete()
        messages.add_message(request, messages.SUCCESS, "Order Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "ordersListChanged"})

    if request.method == 'GET':
        id = request.GET.get('id', '')
        return render(request, "dashboard/partials/delete-order.html", {
            "id": id,
        })


@login_required
def blocked_requests(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")
    reported_users_ref = db.collection("ReportedUsers")

    if request.method == 'POST':
        id = request.POST.get('id', '')
        reported_user = reported_users_ref.document(id).get().to_dict()
        print("Reported User Data: ", reported_user)
        return render(request, 'dashboard/partials/reported-user-detail.html', {
            'detail': reported_user
        })

    results = [item.to_dict() for item in reported_users_ref.get()]
    print("Reported Users Data: ", results)

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())
    ctx['results'] = results

    return render(request, 'dashboard/reported-users.html', ctx)


@login_required
def delete_blocked_request(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        reported_users_ref = db.collection("ReportedUsers")
        reported_users_ref.document(id).delete()
        messages.add_message(request, messages.SUCCESS,
                             "Block Request Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "reporteduserslistListChanged"})

    if request.method == 'GET':
        id = request.GET.get('id', '')
        return render(request, "dashboard/partials/delete-reported-user.html", {
            "id": id,
        })


@login_required
def ads(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")
    carousel_ref = db.collection("carousel").document("images")

    if request.method == 'POST':
        id = request.POST.get('id', '')
        # image = carousel_ref.document(id).get().to_dict()
        print("Ad Data: ", id)
        return render(request, 'dashboard/partials/ad-detail.html', {
            'detail': id
        })

    results = carousel_ref.get().to_dict()["image"]
    print("Ads Data: ", results)

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())
    ctx['results'] = results

    return render(request, 'dashboard/ads.html', ctx)


@login_required
def create_ad(request):
    if request.method == 'POST':
        ad_file = request.FILES.get("ad-file", "")
        print("Ad File: ", ad_file.name)
        blob = bucket.blob(f'pictures/{ad_file.name}')
        # blob.upload_from_filename(ad_file)
        blob.upload_from_file(ad_file, content_type=ad_file.content_type)
        blob.make_public()
        print("URL:", blob.public_url)
        carousel_ref = db.collection("carousel").document("images")
        carousel_ref.update(
            {u'image': firestore.ArrayUnion([blob.public_url])})
        messages.add_message(request, messages.SUCCESS, "Ad Created")
        return HttpResponse(status=204, headers={'HX-Trigger': "adsListChanged"})

    if request.method == 'GET':
        return render(request, "dashboard/partials/create-ad.html", {})


@login_required
def delete_ad(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        carousel_ref = db.collection("carousel").document("images")
        carousel_ref.update({u'image': firestore.ArrayRemove([u''+id])})
        messages.add_message(request, messages.SUCCESS, "Ad Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "adsListChanged"})

    if request.method == 'GET':
        id = request.GET.get('id', '')
        return render(request, "dashboard/partials/delete-ad.html", {
            "id": id,
        })


@login_required
def notifications(request):
    users_ref = db.collection("User")
    menus_ref = db.collection("Menu")
    recipes_ref = db.collection("Recipe")
    orders_ref = db.collection("Order")
    notifications_ref = db.collection("notifications")

    if request.method == 'POST':
        id = request.POST.get('id', '')
        notification = notifications_ref.document(id).get().to_dict()
        print("Notification Data: ", notification)
        return render(request, 'dashboard/partials/notification-detail.html', {
            'detail': notification
        })

    results = {item.id: item.to_dict() for item in notifications_ref.get()}
    print("Notification Data: ", results)

    ctx = {}
    ctx['users_count'] = len(users_ref.get())
    ctx['menus_count'] = len(menus_ref.get())
    ctx['recipes_count'] = len(recipes_ref.get())
    ctx['orders_count'] = len(orders_ref.get())
    ctx['results'] = results

    return render(request, 'dashboard/notifications.html', ctx)


@login_required
def delete_notification(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        print("Notification ID: ", id)
        notifications_ref = db.collection("notifications")
        notifications_ref.document(id).delete()
        messages.add_message(request, messages.SUCCESS, "Notification Deleted")
        return HttpResponse(status=204, headers={'HX-Trigger': "notificationsListChanged"})

    if request.method == 'GET':
        id = request.GET.get('id', '')
        return render(request, "dashboard/partials/delete-notification.html", {
            "id": id,
        })
