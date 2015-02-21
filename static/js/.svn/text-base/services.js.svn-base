'use strict';

app.factory('Book', function($http) {
    function getUrl(arg) {
        return 'http://douban2ucas.sinaapp.com/apis/'+arg;
    }

    return {
        wish: function(callback) {
            return $http.get(getUrl('wish')).success(callback);
        },
        read: function(callback) {
            return $http.get(getUrl('read')).success(callback);
        },
        reading: function(callback) {
            return $http.get(getUrl('reading')).success(callback);
        },
        ucas: function(isbn, callback) {
            return $http.get(getUrl('ucas/'+isbn)).success(callback);
        },
    }
});