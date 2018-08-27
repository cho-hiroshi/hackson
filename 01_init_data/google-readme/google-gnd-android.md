# Ground for Android

Ground is a map-centric data collection platform for occasionally
connected devices.

This is not an officially supported Google product; it is currently
being developed by volunteers on a best-effort basis.

The project is currently undergoing major architectural and UI changes.
Please check back periodically for updates. The stable demo version is
in branch [`prototype`](https://github.com/google/gnd-android/tree/prototype).

## Initial build configuration

### Add Google Maps API Key(s)

Create google_maps_api.xml files in gnd/src/debug/res/values and
gnd/src/release/res/values, replacing API_KEY with debug and release Google Maps
API keys:

``` xml
<resources>
  <string name="google_maps_key" templateMergeStrategy="preserve"
  translatable="false">API_KEY</string>
</resources>
```

You can generate new keys at:

  https://developers.google.com/maps/documentation/android-api/signup.

Be sure the SHA-1 certificate fingerprint described in the API key generation instructions is  
registered with package name ```com.google.android.gnd``` in:

  https://console.cloud.google.com/apis/credentials

You can find the SHA-1 of the debug key generated by Android Studio with:

```
$ keytool -list -v -keystore "$HOME/.android/debug.keystore" \
  -alias androiddebugkey \
  -storepass android -keypass android
```

### Set up Firebase

1. Create a new Firebase project at:

    https://console.firebase.google.com/

2. Save config file for Android app to gnd/google-services.json:

    https://support.google.com/firebase/answer/7015592

This includes the API key and URL for your new Firebase project.