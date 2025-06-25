var app=angular.module("app1",['ngRoute']);
app.config(function($routeProvider)
{
		$routeProvider
		.when("/home.html",
		{
			templateUrl:"home.html",
			controller:"c1"
		})
		.when("/about.html",
		{
			templateUrl:"about.html",
			controller:"c2"
		})
		.when("/user.html",
		{
			templateUrl:"user.html",
			controller:"c3"
		})
		.otherwise(
		{
			redirectTo:"/home.html"
		});
		
})

app.controller("c1",function($scope)
	{
		$scope.display="Welcome to home page"
	})
app.controller("c2",function($scope)
	{
		$scope.display="Welcome to About page page"
	})
app.controller("c3",function($scope)
	{
		$scope.display="Welcome to user page"
	})