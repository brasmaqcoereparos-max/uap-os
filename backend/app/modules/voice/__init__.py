"""Proxy package for compatibility.

This package re-exports the public API from the existing
app.modules.Voice package (uppercase). Creating this proxy
avoids duplicating many files while making a lowercase
package available for imports.

These files are auto-generated wrappers that import from
app.modules.Voice.<module>. If you need full physical copies
(without imports), tell me and I can replace the wrappers
with exact file contents instead.
"""

from app.modules.Voice import *
