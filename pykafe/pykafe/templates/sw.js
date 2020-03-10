
/* eslint-env worker,es6 */
/* global workbox */
//importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.3.1/workbox-sw.js');
importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js');

if (workbox) {

    workbox.core.skipWaiting();
    workbox.core.clientsClaim();

    workbox.routing.registerRoute(
        new RegExp('/media/.*'),
        workbox.strategies.staleWhileRevalidate()
    );

    workbox.routing.registerRoute(
        new RegExp('/admin/.*'),
        workbox.strategies.NetworkOnly()
    );

    workbox.routing.registerRoute(
        new RegExp('/pykafe-admin/.*'),
        workbox.strategies.NetworkOnly()
    );

    workbox.routing.registerRoute(
        new RegExp('/rosetta/.*'),
        workbox.strategies.NetworkOnly()
    );

    workbox.routing.registerRoute(
        new RegExp('.*'),
        workbox.strategies.NetworkFirst()
    );

    workbox.routing.registerRoute(
        new RegExp('/static/.*'),
        workbox.strategies.CacheFirst()
    );
    workbox.routing.setDefaultHandler(workbox.strategies.networkOnly());
}
