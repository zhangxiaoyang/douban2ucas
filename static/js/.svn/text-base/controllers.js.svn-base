'use strict';

app.controller('WishController', function($scope, Book) {
    Book.wish(function(data) {
        $scope.books = data;
        $scope.details = {};
        for (var i=0; i < $scope.books.length; i++) {
            $scope.details[$scope.books[i].isbn] = null;
            Book.ucas($scope.books[i].isbn, function(d) {
                $scope.details[d.isbn] = d.details;
            });
        }
    });
});

app.controller('ReadController', function($scope, Book) {
    Book.read(function(data) {
        $scope.books = data;
        $scope.details = {};
        for (var i=0; i < $scope.books.length; i++) {
            $scope.details[$scope.books[i].isbn] = null;
            Book.ucas($scope.books[i].isbn, function(d) {
                $scope.details[d.isbn] = d.details;
            });
        }
    });
});

app.controller('ReadingController', function($scope, Book) {
    Book.reading(function(data) {
        $scope.books = data;
        $scope.details = {};
        for (var i=0; i < $scope.books.length; i++) {
            $scope.details[$scope.books[i].isbn] = null;
            Book.ucas($scope.books[i].isbn, function(d) {
                $scope.details[d.isbn] = d.details;
            });
        }
    });
});

app.controller('NavbarController', function($scope, $location) {
    $scope.getActive = function(path) {
        return $location.url().split('?')[0] == path;
    }
});
