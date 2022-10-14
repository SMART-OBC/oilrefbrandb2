{
    'name': "Online Reservation System",
    'version': "1.0.96",
    'author': "SMART",
    'category': "Tools",
    'summary': "Allow website users to book reservation from the website",
    'license':'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'security/access_security.xml',
        'data/data.xml',
        'data/cron_job.xml',
        'data/pax_person_data.xml',
        'data/dashboard_data.xml',
        'data/time_day_data.xml',
        'views/company.xml',
        'views/reservation_event.xml',
        'views/table_event.xml',
        'views/dashboard_views.xml',
        'views/home_reservation.xml',
        'views/res_config_settings_views.xml',
        'views/time_slot_share.xml',
        # 'views/pax_person.xml',

        # 'views/table_time_slot.xml',
        'views/time_slot_dates.xml',
        'views/time_event.xml',
        'views/website_calendar_views.xml',
        'views/website_calendar_booking_templates.xml',

    ],
    'demo': [],
    'depends': ['base','website', 'calendar','point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            '/website_calendar_booking/static/src/css/ticket_pos.css',
            '/website_calendar_booking/static/src/js/models.js',
            '/website_calendar_booking/static/src/js/Chrome.js',
            '/website_calendar_booking/static/src/js/ReservationButton.js',
            '/website_calendar_booking/static/src/js/TicketScreen/TicketScreen.js',
            '/website_calendar_booking/static/src/js/ReservationDetails/ReservationDetailsEdit.js',
            # 'customer_due_pos/static/src/js/ordrline_extend.js'
        ],
        'web.assets_frontend': [
            '/website_calendar_booking/static/src/css/fullcalendar.css',
            '/website_calendar_booking/static/src/css/booking_n_res_mob.css',
            '/website_calendar_booking/static/src/css/booking_n_reservation.css',
            '/website_calendar_booking/static/src/css/newcalendar.css',
            '/website_calendar_booking/static/src/css/website_calendar_booking.css',
            '/website_calendar_booking/static/src/css/reservation_popup.css',
            '/website_calendar_booking/static/src/css/reservation_main.css',
            '/web/static/lib/moment/moment.js',
            '/website_calendar_booking/static/src/js/booking_n_reservation.js',
            '/website_calendar_booking/static/src/js/fullcalendar.js',
            '/website_calendar_booking/static/src/js/booking_website.js',

        ],
        'web.assets_backend': [
            '/website_calendar_booking/static/src/css/reservation_kanban.css',
        ],
        'web.assets_qweb': [
            '/website_calendar_booking/static/src/xml/Chrome.xml',
            '/website_calendar_booking/static/src/xml/ReservationButton.xml',
            '/website_calendar_booking/static/src/xml/TicketScreen/TicketScreen.xml',
            '/website_calendar_booking/static/src/xml/ReservationDetails/ReservationDetailsEdit.xml',
            '/website_calendar_booking/static/src/xml/website_calendar_booking_modal1.xml'
        ],
    },

    'images':[
        'static/description/1.jpg',
        'static/description/2.jpg',
        'static/description/3.jpg',
        'static/src/img/icons8breakfast64.png'
    ],
    'installable': True,

}
