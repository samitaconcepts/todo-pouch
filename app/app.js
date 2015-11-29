angular.module('Todo', ['angular-pouch', 'ngRoute'])
  .config(function($routeProvider, $locationProvider) {
    'use strict';

    $routeProvider
      .when('/', { 
        controller: 'MainCtrl', 
        templateUrl: '/app/templates/main.html'
      });
    $locationProvider.html5Mode(true);
  });
