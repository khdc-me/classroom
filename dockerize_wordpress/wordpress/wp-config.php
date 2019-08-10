<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'mysql_admin' );

/** MySQL database password */
define( 'DB_PASSWORD', 'mysql_password' );

/** MySQL hostname */
define( 'DB_HOST', 'mysql' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'FqF{l10L&]JYC!`BD8]3n.Z8p]_sDNNAaEIPg_`(f?Te1)@,$:,.:?I[J8p>|^YA' );
define( 'SECURE_AUTH_KEY',  '~(HZ=]uuN)DV%qp?*;cT)FkiW53Tv|v[aQBZeVMC(O5_c%nH]<{W}rIzz{#SNbMN' );
define( 'LOGGED_IN_KEY',    ']G{YZA/7oLD7nQ/3uG% (%%V^UJcTiV>S(S7Ir)2v`!gk#VuGz6<knSXa@{]8@My' );
define( 'NONCE_KEY',        'tPof@n=sF1?h^b:RDAYe&@AMW2sGnfMdxK5wc02-.dXEHO@0y);vxzMXDW<FYEZ{' );
define( 'AUTH_SALT',        '@Da5zQ-|NzUk|ybx0_bBnySXRJ>nVBOg0Bj?Vw]kApO&HbdN;Y%bUhNAIPADe}D{' );
define( 'SECURE_AUTH_SALT', '#mm]ay e]<s3;R!0Cl}1f:PdZZu?hUntjggS5WG#:eYa53UMEFulVCRqx4|C;dQm' );
define( 'LOGGED_IN_SALT',   ':eAYsAn=tF$%cbB4{TKNc:%W]3pu?%l4Yh5r>qe}Eq879V6G`#dxJAK!^QIo0|z0' );
define( 'NONCE_SALT',       'T=C+[Ri2bejP,>^=(&I%ru^Axbl7Lsu_ L{.:FDg$%uT|6 &BU{>oPAM7g~NPFUJ' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once( ABSPATH . 'wp-settings.php' );
