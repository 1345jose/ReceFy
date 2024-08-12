-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 12-08-2024 a las 01:07:00
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `recefy_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user', 1, 'add_miusuario'),
(2, 'Can change user', 1, 'change_miusuario'),
(3, 'Can delete user', 1, 'delete_miusuario'),
(4, 'Can view user', 1, 'view_miusuario'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'contenttypes', 'contenttype'),
(1, 'ReceFy', 'miusuario'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-07 22:22:04.631653'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-08-07 22:22:04.712117'),
(3, 'auth', '0001_initial', '2024-08-07 22:22:05.204822'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-08-07 22:22:05.276326'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-08-07 22:22:05.287326'),
(6, 'auth', '0004_alter_user_username_opts', '2024-08-07 22:22:05.293325'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-08-07 22:22:05.301106'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-08-07 22:22:05.303747'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-08-07 22:22:05.311609'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-08-07 22:22:05.322314'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-08-07 22:22:05.351316'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-08-07 22:22:05.416410'),
(13, 'auth', '0011_update_proxy_permissions', '2024-08-07 22:22:05.428410'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-08-07 22:22:05.436631'),
(15, 'ReceFy', '0001_initial', '2024-08-07 22:22:05.867003'),
(16, 'admin', '0001_initial', '2024-08-07 22:22:06.031271'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-08-07 22:22:06.045077'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-07 22:22:06.056362'),
(19, 'sessions', '0001_initial', '2024-08-07 22:22:06.103681');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1rzwhjn01i4swxuxvn2o7c4kozqx19z4', '.eJxVjDEOwjAMRe-SGUXBISRmZO8ZIrt2SQGlUtNOiLtDpQ6w_vfef5lM61Ly2nTOo5iLgWAOvyNT_9C6EblTvU22n-oyj2w3xe602W4SfV539--gUCvfOsLJoRydCqKHBF7cwJF91ETMgECOg7ACivNRQkhnpcjEaZCEIOb9AQB_OGw:1scd1p:_94uVDAAZ7VwcPcVp0XDMpNoAcyUEJFuMw4lncgbdiI', '2024-08-24 03:44:29.849797'),
('bspa4bl7lyfslmnw2nk1kqfmhgkw1ouz', '.eJxVjDsOwjAQBe_iGlneJf4sJT1nsHb9IQGUSHFSIe5OIqWAdmbee6vI69LHtZU5DlldFIA6_ULh9CzjbvKDx_uk0zQu8yB6T_Rhm75NubyuR_t30HPrtzUZ572Hih0AmkQOREKqaEAy2QLcBR820HGg7CqGsyX0SCiVbC2iPl_bSjdf:1scrCb:68mzbQhZD9ZQhZ4manoV7dU6q5gclAuKaXAfOKcCHPY', '2024-08-24 18:52:33.623409'),
('el7sllj2prligya81x42bfpydwgpvgwc', '.eJxVjEEOwiAQRe_C2pAOlFJcuvcMZIYZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uz8ur0uxGmh9Qd8B3rbdZprusykd4VfdCmrzPL83K4fwcFW_nWXecDA_YuZA8dDxacMU5sj5TGMTgRawYCIrA5o_HsBiFnuCdgK4Dq_QHJNzfB:1sdEd7:wfTDHCaXdKo2I_EbnSl0JatGtDZO6H6L0PEfJ9c02ZE', '2024-08-25 19:53:29.734708'),
('g9jmxpr24246yelufhpvx5lf33buq8xd', '.eJxVjDsOwjAQBe_iGlleJ-sPJT1nsNbOLg6gWMqnQtwdIqWA9s3Me6lE21rTtvCcxkGdFaA6_Y6ZyoOnnQx3mm5Nlzat85j1ruiDLvraBn5eDvfvoNJSvzWyKyycHZnYSyQrPuSMFgA7G5wXJyAQTbZI3qDFwl1XeoAQiw_C6v0BEm034w:1sd3KM:2tCj-XF3iIa7vDJkb9WmLZIhOOVmTquIoaj4_1inpAU', '2024-08-25 07:49:22.648246'),
('iiepx2tk9dk912xnfkc82ygwf49gv2l0', '.eJxVjEEOwiAQRe_C2pAOlFJcuvcMZIYZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uz8ur0uxGmh9Qd8B3rbdZprusykd4VfdCmrzPL83K4fwcFW_nWXecDA_YuZA8dDxacMU5sj5TGMTgRawYCIrA5o_HsBiFnuCdgK4Dq_QHJNzfB:1sdEGY:y-QpxfwPdyAU2oJqpF40L9qA_JP91s14IP07YsZJieE', '2024-08-25 19:30:10.696934'),
('k4xkpcnu5p4k1ufbzvhgfoue7e5obzu2', '.eJxVjDsOwjAQBe_iGlneJf4sJT1nsHb9IQGUSHFSIe5OIqWAdmbee6vI69LHtZU5DlldFIA6_ULh9CzjbvKDx_uk0zQu8yB6T_Rhm75NubyuR_t30HPrtzUZ572Hih0AmkQOREKqaEAy2QLcBR820HGg7CqGsyX0SCiVbC2iPl_bSjdf:1sd2ff:mPCslIID0gTaodWElsn2nqn0tzGm3JYqBZgqGcNthEM', '2024-08-25 07:07:19.899502'),
('ncb35gpgojtvf5rsu6mztrhkop6eoqcv', '.eJxVjDsOwjAQBe_iGlleJ-sPJT1nsNbOLg6gWMqnQtwdIqWA9s3Me6lE21rTtvCcxkGdFaA6_Y6ZyoOnnQx3mm5Nlzat85j1ruiDLvraBn5eDvfvoNJSvzWyKyycHZnYSyQrPuSMFgA7G5wXJyAQTbZI3qDFwl1XeoAQiw_C6v0BEm034w:1scu5P:Mq-LrxoeNgbYCbxbGhY3RUBJQAcmfzN3tPulcAPb_P8', '2024-08-24 21:57:19.070332'),
('rzur22wuid2ltr623i2frhz5mgv6f3a6', '.eJxVjDsOwjAQBe_iGlneJf4sJT1nsHb9IQGUSHFSIe5OIqWAdmbee6vI69LHtZU5DlldFIA6_ULh9CzjbvKDx_uk0zQu8yB6T_Rhm75NubyuR_t30HPrtzUZ572Hih0AmkQOREKqaEAy2QLcBR820HGg7CqGsyX0SCiVbC2iPl_bSjdf:1sc5pU:3jpYg4LuRI17CziXnjmBLK7bAn8ZeuZxKVdZuix7NWs', '2024-08-22 16:17:32.536164');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recefy_miusuario`
--

CREATE TABLE `recefy_miusuario` (
  `id` bigint NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `imagen1` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `imagen2` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `telefono` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `biografia` longtext COLLATE utf8mb4_general_ci,
  `pais` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `idioma` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `edad` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `recefy_miusuario`
--

INSERT INTO `recefy_miusuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `imagen1`, `imagen2`, `telefono`, `fecha_nacimiento`, `biografia`, `pais`, `idioma`, `edad`) VALUES
(1, 'pbkdf2_sha256$720000$rMQ3uozxeao2VE4VkG102o$l0ICePr+0f/RTkBubDlfhbWpTwE7Uv19Urcw8YYJ8+k=', '2024-06-21 23:45:04.033627', 0, 'astrid vasquez', '', '', 'astridvasquez474@gmail.com', 0, 1, '2024-06-20 22:51:31.092187', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'pbkdf2_sha256$600000$75Pu7qWIHpxM90rWNC0uiT$SXxijgmplcXdB0xA4mNPJdf+A7Ra936VesWZdXg2dEc=', '2024-08-11 19:53:29.726872', 1, 'Samuel', 'Samuel', 'Saldarriaga', 'samuelsaldarriaga0510@gmail.com', 1, 1, '2024-06-09 21:08:40.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, 'pbkdf2_sha256$600000$nW0IlTZ1VriVwqVdlloPgu$982deeIVxh/Zw0nCON2whrue0Mo0hCP3SrKbnt2lIiA=', NULL, 0, 'Jordan', 'Jordan', 'Saldarriaga', 'samuelsaldarriagaramirez@outlook.es', 0, 1, '2024-06-11 22:00:07.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'pbkdf2_sha256$720000$Zk2G63EZYTYaSXoPllwtyh$Kuqzep7U4E8FrjDT2Nr1qPawg4KLK9PHiw71vP1tVt4=', '2024-08-11 07:07:19.891505', 0, 'administrador J', 'Jose', 'Vasquez', 'jose.vasquez111@soy.sena.edu.co', 0, 1, '2024-06-20 01:26:33.325113', '', 'perfil_usuario/blank-profile-picture-973460_1280_iOoERcx.webp', '3188158107', '2005-05-12', 'soy jose y este es mi perfil', 'colombia', 'español', 19),
(14, 'pbkdf2_sha256$720000$LG4aR2qleXJ4DI0zMKOUyZ$nhdL7zz8gNSem9yUXnEYX1oZrNCQKHXynp7tkP2jTr8=', '2024-06-21 02:56:38.734563', 0, 'recetarium', '', '', 'recetarium19@gmail.com', 0, 1, '2024-06-21 02:27:33.827665', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, 'pbkdf2_sha256$720000$pAHIvP2N8eWWd855KWfee9$KezI+LQMaPoqFVvsD+NvKQjNOWo9OwuxriFRdqqRdkg=', '2024-08-11 07:49:22.648246', 0, 'yesselopezt0', 'yesse', 'lopez', 'yesselopezt0@gmail.com', 0, 1, '2024-06-21 04:23:51.218468', '', '\r\n', '3052363130', '2006-12-03', 'hola, soy yo, la novia de jose, me gusta dibujar y voy a estudiar diseño grafico', 'Colombia', 'español', NULL),
(16, 'pbkdf2_sha256$720000$kF1NaXTaC7TOU5dchilwlx$PxRMKI69rAeeZsXaoUWLfkp7fMw29Q8BVshnzj3/gLg=', '2024-08-10 04:37:20.173885', 1, 'josevasquez', 'Jose', 'Vasquez', 'josevas1347@gmail.com', 1, 1, '2024-06-23 06:02:59.000000', '', '', '3188158107', '2005-05-13', 'otra cuenta de respaldo de jose vasquez', 'colombia', 'español', 19),
(17, 'pbkdf2_sha256$720000$7HMZXFO8GiikKJ3T5gBAP0$s9R4clzqjRR77CY8txdBTyOlgSM0EtunvTDLjTWo4t8=', '2024-06-23 18:10:51.387258', 0, 'Juan_pablo', '', '', 'jpvasquez0709@gmail.com', 0, 1, '2024-06-23 18:07:10.121081', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20, 'pbkdf2_sha256$720000$bcz9bVo1G5zdDwft2KQnl6$p8lYV9Kn2irgY93yiEtnGGPo3W3KrZ+enbHALfNm8kk=', '2024-08-02 16:12:57.612197', 0, 'laguna', '', '', 'diego1415@gmail.com', 0, 1, '2024-08-02 16:12:33.688595', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21, 'pbkdf2_sha256$720000$nuPGmxYHeiKSpBjXd9SUbb$ZIzYvM7VBwgDzG/m9lkx23h8yorzMYviRCiFqgzkGlE=', '2024-08-10 05:32:31.615387', 0, 'Administrador_jose', '', '', 'user474dh@gmail.com', 0, 1, '2024-08-08 02:16:24.694407', '', 'perfil_usuario/Jose_Manuel_Vasquez_Quirós_1017924366_O.jpeg', '3188158107', '2005-05-13', 'Soy administrador en recefy con samuel saldapapas', 'colombia', 'español', 2),
(24, 'pbkdf2_sha256$720000$c81AZF5TA8G55pVXGOeMWk$G8vVueKN4lMi7++ZxzPi/IsS/yAA/gOu+MOLwW/NBs4=', '2024-08-09 12:36:36.301696', 0, 'TomRamirezG', 'Tomas', 'Ramirez', 'tomramirezg11@gmail.com', 0, 1, '2024-08-09 12:36:02.687989', '', 'perfil_usuario/tom.jpeg', '3023332541', '2006-01-26', 'soy tomas y soy administrador en recefy', 'colombia', 'español', 18),
(25, 'pbkdf2_sha256$720000$yVoHoWYfaG9NRzrfVgHzrp$koGn4fDxt3A4Kp2B0TtqH2D8YrCwcuio5aJE/gBEeeU=', '2024-08-10 03:44:29.849797', 0, 'Juanjose2901', 'Juan jose', 'Vasquez ', 'juanjose290101@gmail.com', 0, 1, '2024-08-10 03:42:12.082837', '', '', '3016513948', '2024-08-09', 'Soy juanjo', 'Colombia', 'español', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recefy_miusuario_groups`
--

CREATE TABLE `recefy_miusuario_groups` (
  `id` bigint NOT NULL,
  `miusuario_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recefy_miusuario_user_permissions`
--

CREATE TABLE `recefy_miusuario_user_permissions` (
  `id` bigint NOT NULL,
  `miusuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_comentarios`
--

CREATE TABLE `tbl_comentarios` (
  `id` int NOT NULL,
  `receta_id` int NOT NULL,
  `usuario_id` bigint NOT NULL,
  `contenido` varchar(1500) NOT NULL,
  `fecha_creacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `me_gusta` int UNSIGNED DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `tbl_comentarios`
--

INSERT INTO `tbl_comentarios` (`id`, `receta_id`, `usuario_id`, `contenido`, `fecha_creacion`, `me_gusta`) VALUES
(1, 140, 11, 'los pancakes me gustaron mucho ', '2024-08-11 07:09:02', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_like_c`
--

CREATE TABLE `tbl_like_c` (
  `id` int NOT NULL,
  `comentario_id` int DEFAULT NULL,
  `usuario_id` bigint DEFAULT NULL,
  `fecha` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_plan_nutricional`
--

CREATE TABLE `tbl_plan_nutricional` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` bigint NOT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `desayuno_domingo` text COLLATE utf8mb4_general_ci,
  `media_manana_domingo` text COLLATE utf8mb4_general_ci,
  `almuerzo_domingo` text COLLATE utf8mb4_general_ci,
  `merienda_domingo` text COLLATE utf8mb4_general_ci,
  `cena_domingo` text COLLATE utf8mb4_general_ci,
  `desayuno_lunes` text COLLATE utf8mb4_general_ci,
  `media_manana_lunes` text COLLATE utf8mb4_general_ci,
  `almuerzo_lunes` text COLLATE utf8mb4_general_ci,
  `merienda_lunes` text COLLATE utf8mb4_general_ci,
  `cena_lunes` text COLLATE utf8mb4_general_ci,
  `desayuno_martes` text COLLATE utf8mb4_general_ci,
  `media_manana_martes` text COLLATE utf8mb4_general_ci,
  `almuerzo_martes` text COLLATE utf8mb4_general_ci,
  `merienda_martes` text COLLATE utf8mb4_general_ci,
  `cena_martes` text COLLATE utf8mb4_general_ci,
  `desayuno_miercoles` text COLLATE utf8mb4_general_ci,
  `media_manana_miercoles` text COLLATE utf8mb4_general_ci,
  `almuerzo_miercoles` text COLLATE utf8mb4_general_ci,
  `merienda_miercoles` text COLLATE utf8mb4_general_ci,
  `cena_miercoles` text COLLATE utf8mb4_general_ci,
  `desayuno_jueves` text COLLATE utf8mb4_general_ci,
  `media_manana_jueves` text COLLATE utf8mb4_general_ci,
  `almuerzo_jueves` text COLLATE utf8mb4_general_ci,
  `merienda_jueves` text COLLATE utf8mb4_general_ci,
  `cena_jueves` text COLLATE utf8mb4_general_ci,
  `desayuno_viernes` text COLLATE utf8mb4_general_ci,
  `media_manana_viernes` text COLLATE utf8mb4_general_ci,
  `almuerzo_viernes` text COLLATE utf8mb4_general_ci,
  `merienda_viernes` text COLLATE utf8mb4_general_ci,
  `cena_viernes` text COLLATE utf8mb4_general_ci,
  `desayuno_sabado` text COLLATE utf8mb4_general_ci,
  `media_manana_sabado` text COLLATE utf8mb4_general_ci,
  `almuerzo_sabado` text COLLATE utf8mb4_general_ci,
  `merienda_sabado` text COLLATE utf8mb4_general_ci,
  `cena_sabado` text COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_plan_nutricional`
--

INSERT INTO `tbl_plan_nutricional` (`id`, `nombre`, `user_id`, `fecha_creacion`, `desayuno_domingo`, `media_manana_domingo`, `almuerzo_domingo`, `merienda_domingo`, `cena_domingo`, `desayuno_lunes`, `media_manana_lunes`, `almuerzo_lunes`, `merienda_lunes`, `cena_lunes`, `desayuno_martes`, `media_manana_martes`, `almuerzo_martes`, `merienda_martes`, `cena_martes`, `desayuno_miercoles`, `media_manana_miercoles`, `almuerzo_miercoles`, `merienda_miercoles`, `cena_miercoles`, `desayuno_jueves`, `media_manana_jueves`, `almuerzo_jueves`, `merienda_jueves`, `cena_jueves`, `desayuno_viernes`, `media_manana_viernes`, `almuerzo_viernes`, `merienda_viernes`, `cena_viernes`, `desayuno_sabado`, `media_manana_sabado`, `almuerzo_sabado`, `merienda_sabado`, `cena_sabado`) VALUES
(8, 'hola', 7, '2024-08-12 04:30:22', 'Ejemplo 1', 'Ejemplo 2', 'Ejemplo 3', 'ejemplo 4', 'ejemplo 5', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'aa', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'),
(9, 'Calendario Saldarriaga', 7, '2024-08-12 05:45:12', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_recetas`
--

CREATE TABLE `tbl_recetas` (
  `id_receta` int NOT NULL,
  `nombre_plato` varchar(50) NOT NULL,
  `categoria` varchar(255) NOT NULL,
  `temporada` varchar(255) NOT NULL,
  `origen` varchar(255) NOT NULL,
  `ingredientes` varchar(225) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `instrucciones` varchar(255) NOT NULL,
  `tiempo_preparacion` varchar(10) NOT NULL,
  `dificultad` varchar(20) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `fecha_registro_receta` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `usuario_id` bigint DEFAULT NULL,
  `status` varchar(255) DEFAULT 'habilitado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `tbl_recetas`
--

INSERT INTO `tbl_recetas` (`id_receta`, `nombre_plato`, `categoria`, `temporada`, `origen`, `ingredientes`, `descripcion`, `instrucciones`, `tiempo_preparacion`, `dificultad`, `imagen`, `fecha_registro_receta`, `usuario_id`, `status`) VALUES
(125, 'Tacos de Pescado', 'Tacos', 'Primavera', 'México', 'Pescado, Tortillas, Col, Salsa de yogur, Limón, Especias', 'Deliciosos tacos de pescado con salsa fresca de yogur.', 'Marinar pescado, cocinar, preparar salsa, calentar tortillas, armar tacos.', '30', 'Fácil', 'recetas/tacos_pescados.jpg', '2024-06-25 23:24:44', 1, ''),
(126, 'Spaghetti a la Boloñesa', 'Pasta', 'Invierno', 'Italia', 'Spaghetti, Carne molida, Tomate, Cebolla, Zanahoria, Apio, Ajo, Vino tinto, Especias', 'Clásica receta italiana de pasta con salsa boloñesa.', 'Cocinar carne, agregar verduras, vino y tomate, cocinar spaghetti, mezclar.', '45', 'Media', 'recetas/spaghetti_bolonesa.jpg', '2024-06-25 23:24:44', 1, ''),
(127, 'Sushi de Salmón', 'Sushi', 'Todo el año', 'Japón', 'Arroz para sushi, Salmón, Alga nori, Vinagre de arroz, Azúcar, Sal', 'Tradicional sushi de salmón fresco.', 'Cocinar arroz, cortar salmón, colocar en alga nori, enrollar, cortar.', '40', 'Difícil', 'recetas/sushi_salmon.jpg', '2024-06-25 23:24:44', 1, ''),
(128, 'Brownies de Chocolate', 'Postre', 'Todo el año', 'Estados Unidos', 'Chocolate, Mantequilla, Azúcar, Harina, Huevos, Nueces', 'Deliciosos brownies de chocolate con nueces.', 'Derretir chocolate y mantequilla, mezclar con azúcar y huevos, agregar harina y nueces, hornear.', '60', 'Media', 'recetas/brownies_chocolate.jpg', '2024-06-25 23:24:44', 1, ''),
(129, 'Pollo al Curry', 'Plato Principal', 'Otoño', 'India', 'Pollo, Cebolla, Ajo, Jengibre, Tomate, Leche de coco, Especias de curry, Cilantro', 'Delicioso pollo al curry con una salsa cremosa de leche de coco.', 'Sofreír cebolla, ajo y jengibre, agregar especias, pollo, tomate y leche de coco, cocinar a fuego lento, decorar con cilantro.', '50', 'Media', 'recetas/curry.jpg', '2024-06-25 23:24:44', 1, ''),
(130, 'Ensalada César', 'Ensalada', 'Verano', 'Italia', 'Lechuga, Pollo, Crutones, Queso parmesano, Aderezo César', 'Clásica ensalada César con pollo y crutones.', 'Cortar lechuga, cocinar pollo, mezclar ingredientes y aderezo.', '20', 'Fácil', 'recetas/ensalada_cesar.jpg', '2024-06-25 23:24:44', 1, ''),
(131, 'Paella', 'Plato Principal', 'Verano', 'España', 'Arroz, Pollo, Conejo, Judías verdes, Garrofón, Tomate, Aceite de oliva, Azafrán, Caldo de pollo', 'Auténtica paella valenciana.', 'Sofreír carnes y verduras, agregar arroz y caldo, cocinar hasta que el arroz esté en su punto.', '90', 'Difícil', 'recetas/paella.jpg', '2024-06-25 23:24:44', 1, ''),
(132, 'Hamburguesa Clásica', 'Sandwich', 'Todo el año', 'Estados Unidos', 'Carne de res, Pan de hamburguesa, Lechuga, Tomate, Cebolla, Queso, Salsa de tomate, Mostaza', 'Clásica hamburguesa americana con todos los acompañamientos.', 'Formar y cocinar la carne, tostar pan, montar la hamburguesa con los ingredientes.', '30', 'Fácil', 'recetas/hamburguesa.jpg', '2024-06-25 23:24:44', 1, ''),
(133, 'Gazpacho', 'Sopa', 'Verano', 'España', 'Tomate, Pepino, Pimiento, Ajo, Aceite de oliva, Vinagre, Sal', 'Refrescante sopa fría de tomate.', 'Triturar todos los ingredientes hasta obtener una sopa homogénea, enfriar.', '20', 'Fácil', 'recetas/gazpacho_andaluz.jpeg', '2024-06-25 23:24:44', 1, ''),
(134, 'Pizza Margarita', 'Pizza', 'Todo el año', 'Italia', 'Masa de pizza, Tomate, Mozzarella, Albahaca, Aceite de oliva', 'Clásica pizza italiana con tomate, mozzarella y albahaca.', 'Preparar masa, agregar tomate y mozzarella, hornear, decorar con albahaca.', '40', 'Media', 'recetas/pizza.jpg', '2024-06-25 23:24:44', 1, ''),
(135, 'Sopa de Miso', 'Sopa', 'Invierno', 'Japón', 'Pasta de miso, Tofu, Alga wakame, Cebolla verde, Dashi', 'Sopa japonesa de miso con tofu y alga.', 'Disolver miso en dashi caliente, agregar tofu y alga, servir con cebolla verde.', '15', 'Fácil', 'recetas/miso.jpg', '2024-06-25 23:24:44', 1, ''),
(136, 'Ceviche', 'Entrante', 'Verano', 'Perú', 'Pescado blanco, Limón, Cebolla, Cilantro, Ají, Sal', 'Fresco ceviche peruano de pescado marinado en limón.', 'Marinar pescado en limón, mezclar con cebolla, cilantro y ají, servir frío.', '25', 'Fácil', 'recetas/ceviche_camaron.jpg', '2024-06-25 23:24:44', 1, ''),
(137, 'Tarta de Manzana', 'Postre', 'Otoño', 'Francia', 'Masa de tarta, Manzanas, Azúcar, Canela, Mantequilla', 'Tarta de manzana clásica francesa.', 'Preparar masa, cortar manzanas, montar la tarta, espolvorear azúcar y canela, hornear.', '60', 'Media', 'recetas/tarta.jpeg', '2024-06-25 23:24:44', 1, ''),
(138, 'Falafel', 'Entrante', 'Todo el año', 'Medio Oriente', 'Garbanzos, Cebolla, Ajo, Perejil, Cilantro, Especias', 'Deliciosas bolitas de garbanzo fritas.', 'Triturar garbanzos y mezclarlos con cebolla, ajo y especias, formar bolitas, freír.', '45', 'Media', 'recetas/falafel.jpg', '2024-06-25 23:24:44', 1, ''),
(139, 'Empanadas Argentinas', 'Entrante', 'Todo el año', 'Argentina', 'Harina, Carne picada, Cebolla, Huevo, Aceitunas, Especias', 'Empanadas argentinas tradicionales con relleno de carne.', 'Preparar masa, cocinar relleno, formar empanadas, hornear.', '70', 'Media', 'recetas/empanadas-argentinas.jpg', '2024-06-25 23:24:44', 1, ''),
(140, 'Pancakes', 'Desayuno', 'Todo el año', 'Estados Unidos', 'Harina, Leche, Huevo, Mantequilla, Azúcar, Polvo de hornear', 'Pancakes esponjosos perfectos para el desayuno.', 'Mezclar ingredientes, cocinar en sartén caliente, servir con mantequilla y jarabe.', '20', 'Fácil', 'recetas/pancakes.jpg', '2024-06-25 23:24:44', 1, ''),
(141, 'Curry de Garbanzos', 'Plato Principal', 'Invierno', 'India', 'Garbanzos, Tomate, Cebolla, Ajo, Jengibre, Leche de coco, Especias de curry', 'Curry de garbanzos con una rica y cremosa salsa de curry.', 'Sofreír cebolla, ajo y jengibre, agregar especias, tomate, garbanzos y leche de coco, cocinar a fuego lento.', '50', 'Media', 'recetas/garbanzos.webp', '2024-06-25 23:24:44', 1, ''),
(143, 'frijoles', 'Plato principal', 'fechas especiales', 'colombia', 'frijoles , arroz, agua, platano, zanahoria, chicharron , huevos, arepa, carne molida ', 'frijoles rancheros muy ricos', 'debes hacer la receta de la siguiente manera', '120', 'alta', 'recetas/chili_con_carne.jpg', '2024-06-26 19:15:43', 15, ''),
(147, 'papas', 'Postres', 'fechas especiales', 'de mi casa', 'no se', 'pa morir', 'compre las papas', '5', 'baja', 'recetas/papas_limon.jpg', '2024-08-02 21:14:46', 20, 'habilitado'),
(149, 'sakjajkd', 'Desayuno\r\n', 'fechas especiales', 'dakakdad', 'lskdladkla', 'sa,saks', 'dalalkd', '23', 'media', 'recetas/7cIt_zfNFy0D.gif', '2024-08-11 04:06:40', 11, 'habilitado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_ReceFy_miusuario_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `recefy_miusuario`
--
ALTER TABLE `recefy_miusuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `recefy_miusuario_groups`
--
ALTER TABLE `recefy_miusuario_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ReceFy_miusuario_groups_miusuario_id_group_id_d95e83bd_uniq` (`miusuario_id`,`group_id`),
  ADD KEY `ReceFy_miusuario_groups_group_id_f3d55ce8_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `recefy_miusuario_user_permissions`
--
ALTER TABLE `recefy_miusuario_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ReceFy_miusuario_user_pe_miusuario_id_permission__886e073f_uniq` (`miusuario_id`,`permission_id`),
  ADD KEY `ReceFy_miusuario_use_permission_id_e73ce8a2_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `tbl_comentarios`
--
ALTER TABLE `tbl_comentarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `receta_id` (`receta_id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `tbl_like_c`
--
ALTER TABLE `tbl_like_c`
  ADD PRIMARY KEY (`id`),
  ADD KEY `comentario_id` (`comentario_id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `tbl_plan_nutricional`
--
ALTER TABLE `tbl_plan_nutricional`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indices de la tabla `tbl_recetas`
--
ALTER TABLE `tbl_recetas`
  ADD PRIMARY KEY (`id_receta`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `recefy_miusuario`
--
ALTER TABLE `recefy_miusuario`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `recefy_miusuario_groups`
--
ALTER TABLE `recefy_miusuario_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `recefy_miusuario_user_permissions`
--
ALTER TABLE `recefy_miusuario_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_comentarios`
--
ALTER TABLE `tbl_comentarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tbl_like_c`
--
ALTER TABLE `tbl_like_c`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tbl_plan_nutricional`
--
ALTER TABLE `tbl_plan_nutricional`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tbl_recetas`
--
ALTER TABLE `tbl_recetas`
  MODIFY `id_receta` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=150;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_ReceFy_miusuario_id` FOREIGN KEY (`user_id`) REFERENCES `recefy_miusuario` (`id`);

--
-- Filtros para la tabla `recefy_miusuario_groups`
--
ALTER TABLE `recefy_miusuario_groups`
  ADD CONSTRAINT `ReceFy_miusuario_gro_miusuario_id_bc46a83a_fk_ReceFy_mi` FOREIGN KEY (`miusuario_id`) REFERENCES `recefy_miusuario` (`id`),
  ADD CONSTRAINT `ReceFy_miusuario_groups_group_id_f3d55ce8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `recefy_miusuario_user_permissions`
--
ALTER TABLE `recefy_miusuario_user_permissions`
  ADD CONSTRAINT `ReceFy_miusuario_use_miusuario_id_f0e050c3_fk_ReceFy_mi` FOREIGN KEY (`miusuario_id`) REFERENCES `recefy_miusuario` (`id`),
  ADD CONSTRAINT `ReceFy_miusuario_use_permission_id_e73ce8a2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `tbl_comentarios`
--
ALTER TABLE `tbl_comentarios`
  ADD CONSTRAINT `tbl_comentarios_ibfk_1` FOREIGN KEY (`receta_id`) REFERENCES `tbl_recetas` (`id_receta`),
  ADD CONSTRAINT `tbl_comentarios_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `recefy_miusuario` (`id`);

--
-- Filtros para la tabla `tbl_like_c`
--
ALTER TABLE `tbl_like_c`
  ADD CONSTRAINT `tbl_like_c_ibfk_1` FOREIGN KEY (`comentario_id`) REFERENCES `tbl_comentarios` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tbl_like_c_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `recefy_miusuario` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `tbl_plan_nutricional`
--
ALTER TABLE `tbl_plan_nutricional`
  ADD CONSTRAINT `tbl_plan_nutricional_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `recefy_miusuario` (`id`);

--
-- Filtros para la tabla `tbl_recetas`
--
ALTER TABLE `tbl_recetas`
  ADD CONSTRAINT `tbl_recetas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `recefy_miusuario` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
