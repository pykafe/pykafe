
/* eslint-env worker,es6 */
/* global workbox */
importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.3.1/workbox-sw.js');

if (workbox) {
    workbox.routing.registerRoute(
        new RegExp('/media/.*'),
        workbox.strategies.staleWhileRevalidate()
      );

    workbox.routing.registerRoute(
        new RegExp('/static/.*'),
        workbox.strategies.CacheFirst()
      );

    workbox.routing.registerRoute(
        new RegExp('/accounts|admin)/.*'),
        workbox.strategies.NetworkOnly()
    );

    workbox.routing.registerRoute(
        new RegExp('.*'),
        workbox.strategies.NetworkFirst()
    );

}
