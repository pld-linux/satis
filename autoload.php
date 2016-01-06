<?php
$phpDir = defined('PHP_DATADIR') && PHP_DATADIR ? PHP_DATADIR . '/php' : '/usr/share/php';
$pearDir = defined('PEAR_INSTALL_DIR') && PEAR_INSTALL_DIR ? PEAR_INSTALL_DIR : '/usr/share/pear';

// Use Symfony autoloader
if (!isset($loader) || !($loader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once $phpDir . '/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $loader = new \Symfony\Component\ClassLoader\ClassLoader();
    $loader->register();
}

$baseDir = dirname(__DIR__);

$loader->addPrefixes(array(
    'Composer\\Satis\\' => $baseDir,

    // Dependencies
    'Twig' => $pearDir,
));

// Dependencies
require_once $phpDir . '/Composer/autoload.php';

return $loader;
