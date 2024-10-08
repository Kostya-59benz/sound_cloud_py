from django.urls import path, include
from . import views


urlpatterns = [
    path('genre/', views.GenreView.as_view(),name='genres'),

    path('license/', views.LicenseView.as_view({'get': 'list', 'post': 'create'}), name='license'),
    path('license/<int:pk>/', views.LicenseView.as_view({'put': 'update', 'delete': 'destroy'}), name='license_change'),
 

    path('album/', views.AlbumView.as_view({'get': 'list', 'post': 'create'}), name='album'),
    path('album/<int:pk>/', views.AlbumView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('author-album/<int:pk>/', views.PubliAlbumView.as_view()),

    path('track/', views.TrackView.as_view({'get': 'list', 'post': 'create'}), name='tracks'),
    path('track/<int:pk>/', views.TrackView.as_view({'put': 'update', 'delete': 'destroy'})),


    path('stream-track/<int:pk>/', views.StreamingFileView.as_view()),
    path('download-track/<int:pk>/', views.DownloadTrackView.as_view()),

    path('track-list/', views.TrackListView.as_view()),
    path('author-track-list/<int:pk>/', views.AuthorTrackListView.as_view()),
    

    path('stream-author-track/<int:pk>/', views.StreamingFileAuthorView.as_view()),


    path('comments/', views.CommentAuthorView.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', views.CommentAuthorView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('comments_by_track/<int:pk>/', views.CommentView.as_view({'get': 'list'})),


    path('playlist/', views.PlayListView.as_view({'get': 'list', 'post': 'create'})),
    path('playlist/<int:pk>/', views.PlayListView.as_view({'put': 'update', 'delete': 'destroy'})),
]