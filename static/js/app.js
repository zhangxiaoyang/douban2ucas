'use strict';

var app = angular.module('uiApp', []);
app.config(function ($routeProvider) {
    $routeProvider
        .when('/home',
            {
                templateUrl: "/static/partials/home.html"
            })
        .when('/wish',
            {
                controller: 'WishController',
                templateUrl: '/static/partials/wish.html'
            })
        .when('/read',
            {
                controller: 'ReadController',
                templateUrl: '/static/partials/wish.html'
            })
        .when('/reading',
            {
                controller: 'ReadingController',
                templateUrl: '/static/partials/wish.html'
            })
        .otherwise({ redirectTo: '/home' });
});
