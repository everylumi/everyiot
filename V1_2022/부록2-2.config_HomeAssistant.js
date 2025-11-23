var config = {
	address: "localhost",
	port: 8080,
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],

	language: "ko",
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
						symbol: "calendar-check",
						url: "https://calendar.google.com/calendar/ical/ko.south_korea%23holiday%40group.v.calendar.google.com/public/basic.ics"
					}
				],
				maximumEntries: 5
			}
		},
		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "Seoul, KR",
				locationID: "",
				appid: "",
				showHumidity: true,
				showFeelsLike: false,
				showWindDirection: false
			}
		},
		{
			module: "weatherforecast",
			position: "top_right",
			header: "weatherforecast",
			config: {
				location: "Seoul, KR",
				locationID: "",
				appid: ""
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			disabled: true,
			config: {
				feeds: [
					{
						title: "Google News",
						url: "https://news.google.com/news/rss/?ned=kr&gl=KR&hl=ko",
					},
				],
				showSourceTitle: true,
				showPublishDate: true,
				showDescription: false
			}
		},

		{
			module: "MMM-HomeAssistant-Touch",
			position: "bottom_bar",
			disabled: false,

			config: {
				host: "http://192.168.219.205",
				port: 8123, 
				token: "Home Assistant 토큰키 입력",
				ignoreCert: false,
				entities: ["switch.switch", "sensor.humidity", "sensor.temperature"]
			},	
		},	
	]

};

if (typeof module !== "undefined") {module.exports = config;}
