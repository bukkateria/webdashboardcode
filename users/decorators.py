from functools import wraps

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.shortcuts import redirect


def agent_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="account_login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_agent,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def is_aggregator_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="account_login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_aggregator,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def merchant_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="account_login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_merchant,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# def lawyer_or_subscriber_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='account_login'):
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and (u.is_lawyer or u.is_subscriber),
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


def admin_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="account_login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin or u.is_merchant,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def is_user_profile_complete(function=None, redirect_url=None):
    actual_decorator = user_passes_test(
        lambda user: user.is_profile_complete,
        login_url=redirect_url,
        redirect_field_name=None,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def check_profile(redirect_to=None, host=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.profile.is_profile_complete:
                return view_func(request, *args, **kwargs)
            else:
                return redirect(reverse(redirect_to, host=host))

        return _wrapped_view

    return decorator
