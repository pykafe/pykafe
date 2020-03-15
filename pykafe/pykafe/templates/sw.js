
/* eslint-env worker,es6 */
/* global workbox */
importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.3.1/workbox-sw.js');
//importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js');

if (workbox) {

    workbox.routing.registerRoute(
        new RegExp('/media/.*'),
        workbox.strategies.staleWhileRevalidate()
    );

    workbox.routing.registerRoute(
        new RegExp('.*'),
        workbox.strategies.networkFirst()
    );

    workbox.routing.registerRoute(
        new RegExp('/static/.*'),
        workbox.strategies.cacheFirst()
    );

    workbox.routing.registerRoute(
        new RegExp('/admin/.*'),
        workbox.strategies.networkOnly()
    );

    workbox.routing.registerRoute(
        new RegExp('/rosetta/.*'),
        workbox.strategies.networkOnly()
    );

    workbox.routing.registerRoute(
        new RegExp('/pykafe-admin/.*'),
        workbox.strategies.networkOnly()
    );
}
