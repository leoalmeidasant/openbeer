PGDMP     )    6                u            beer    9.6.2    9.6.2     �	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �	          0    17197    address 
   TABLE DATA               c   COPY address (id, zip_code, number, street, district, created_at, updated_at, user_id) FROM stdin;
    public       postgres    false    190          �	           0    0    address_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('address_id_seq', 3, true);
            public       postgres    false    189            �	          0    17184    admins 
   TABLE DATA               L   COPY admins (id, name, email, password, created_at, updated_at) FROM stdin;
    public       postgres    false    188   �       �	           0    0    admins_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('admins_id_seq', 1, false);
            public       postgres    false    187            �	          0    20181    alembic_version 
   TABLE DATA               /   COPY alembic_version (version_num) FROM stdin;
    public       postgres    false    201   �       �	          0    17208    beers 
   TABLE DATA               e   COPY beers (id, name, description, value, type, quantity, created_at, updated_at, image) FROM stdin;
    public       postgres    false    192   �       �	           0    0    beers_id_seq    SEQUENCE SET     4   SELECT pg_catalog.setval('beers_id_seq', 32, true);
            public       postgres    false    191            �	          0    17241    item_orders 
   TABLE DATA               5   COPY item_orders (id, item_id, order_id) FROM stdin;
    public       postgres    false    198   |       �	           0    0    item_orders_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('item_orders_id_seq', 1, false);
            public       postgres    false    197            �	          0    17249    items 
   TABLE DATA               G   COPY items (id, beer_id, snack_id, created_at, updated_at) FROM stdin;
    public       postgres    false    200   �       �	           0    0    items_id_seq    SEQUENCE SET     4   SELECT pg_catalog.setval('items_id_seq', 1, false);
            public       postgres    false    199            �	          0    17230    orders 
   TABLE DATA               ^   COPY orders (id, fare, order_date, payment_form, user_id, created_at, updated_at) FROM stdin;
    public       postgres    false    196   �       �	           0    0    orders_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('orders_id_seq', 1, false);
            public       postgres    false    195            �	          0    17219    snacks 
   TABLE DATA               _   COPY snacks (id, name, description, value, type, quantity, created_at, updated_at) FROM stdin;
    public       postgres    false    194   �       �	           0    0    snacks_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('snacks_id_seq', 1, false);
            public       postgres    false    193            �	          0    17171    users 
   TABLE DATA               n   COPY users (id, name, lastname, email, password, confirm_password, phone, created_at, updated_at) FROM stdin;
    public       postgres    false    186   �       �	           0    0    users_id_seq    SEQUENCE SET     3   SELECT pg_catalog.setval('users_id_seq', 7, true);
            public       postgres    false    185            �	   a   x�3�057234�416�t,�Sp�+����Wp+MO��J
�'��r�����!3M��(5�l��1̈Լ̔Dtc0L12Bf�s��qqq �Y1�      �	      x������ � �      �	      x������ � �      �	   �   x���M�0���S��R*���1&��� ��К9�B��7�7����p{�wl.-�|�<�S�8�A�,�=&� Z��U~�T�Gp4=����M,��X�Ri{Y#-Ɩ*�o;8�R�B���Y��O��2����ig�;^�ƓiV�+�t�?x7�i4F\}B��Ba�      �	      x������ � �      �	      x������ � �      �	      x������ � �      �	      x������ � �      �	   �   x�3��I��K,J��LIUp��M�LITN�+�/�́J�%B�Rs3s���s9�����������؄����\��D����eF�|�M6'��b��CfrN~i
�SKehhbnjjill	7�������� �Q)     