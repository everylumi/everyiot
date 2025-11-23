let config = {
	address: "localhost",

	port: 8080,
	basePath: "/",	

	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],


	useHttps: false,
	httpsPrivateKey: "",
	httpsCertificate: "",

	language: "ko",
	locale: "en-US",

	logLevel: ["INFO", "LOG", "WARN", "ERROR"],
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "대한민국 공휴일",
			position: "top_left",
			config: {
				calendars: [
					{
						fetchInterval: 7 * 24 * 60 * 60 * 1000,
						symbol: "calendar-check",
						url: "https://calendar.google.com/calendar/ical/ko.south_korea%23holiday%40group.v.calendar.google.com/public/basic.ics"
					}
				],
				maximumEntries: 5
			}
		},
		{
			module: "compliments",
			position: "lower_third",
			disabled: true
			
		},
		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openmeteo",
				type: "current",
				lat: 37.565577,
				lon: 126.978082
			}
		},
		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				weatherProvider: "openmeteo",
				type: "forecast",
				lat: 37.6583599,
				lon: 126.8320201
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "New York Times",
						url: "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
					},
					{
						title: "Google News",
						url: "https://news.google.com/news/rss/?ned=kr&gl=KR&hl=ko",
					},
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true,
				showDescription: false
			}
		},
	]
};

if (typeof module !== "undefined") { module.exports = config; }
