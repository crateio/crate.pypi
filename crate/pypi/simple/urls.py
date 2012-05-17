from django.conf.urls import patterns, url

from crate.pypi.simple.views import PackageDetail, PackageServerSig

handler404 = "crate.pypi.simple.views.not_found"

urlpatterns = patterns("",
    url(r"^$", "crate.pypi.simple.views.simple_redirect"),
    url(r"^simple/$", "crate.pypi.simple.views.package_index", name="pypi_package_index"),
    url(r"^simple/(?P<slug>[^/]+)/$", PackageDetail.as_view(), name="pypi_package_detail"),
    url(r"^packages/.+/(?P<filename>[^/]+)$", "crate.pypi.simple.views.file_redirect", name="pypi_file_redirect"),
    url(r"^serversig/(?P<slug>[^/]+)/$", PackageServerSig.as_view(), name="pypi_package_serversig"),
    url(r"^last-modified/?$", "crate.pypi.simple.views.last_modified"),
)
