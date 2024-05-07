r = """FESCAR-10 com.alibaba.fescar.core.model.BranchType 80.0% 90.0% 80.0% 90.0% 80.0% 90.0%
FESCAR-12 com.alibaba.fescar.core.rpc.netty.RpcServerHandler 100.0% 100.0% 87.5% 87.5% 100.0% 100.0%
FESCAR-13 com.alibaba.fescar.core.exception.TransactionExceptionCode 100.0% 100.0% 100.0% 100.0% 100.0% 100.0%
FESCAR-15 com.alibaba.fescar.core.rpc.netty.RpcServer 0.8% 0.7% 0.0% 0.0% 0.0% 0.0%
FESCAR-17 com.alibaba.fescar.core.protocol.transaction.GlobalBeginResponse 99.4% 99.4% 100.0% 100.0% 90.0% 90.0%
FESCAR-2 com.alibaba.fescar.core.service.ServiceManagerStaticConfigImpl 20.5% 25.8% 0.0% 0.0% 0.0% 0.0%
FESCAR-23 com.alibaba.fescar.core.protocol.MergeResultMessage 90.5% 60.5% 76.4% 50.0% 0.0% 0.0%
FESCAR-25 com.alibaba.fescar.core.rpc.netty.RmMessageListener 46.9% 37.5% 62.5% 48.8% 22.2% 17.8%
FESCAR-28 com.alibaba.fescar.core.rpc.ClientType 90.0% 100.0% 90.0% 100.0% 90.0% 100.0%
FESCAR-32 com.alibaba.fescar.core.protocol.transaction.BranchRegisterRequest 97.7% 89.2% 94.4% 87.5% 95.2% 78.3%
FESCAR-33 com.alibaba.fescar.core.model.GlobalStatus 100.0% 100.0% 100.0% 100.0% 100.0% 100.0%
FESCAR-34 com.alibaba.fescar.core.protocol.ResultCode 90.0% 100.0% 90.0% 100.0% 90.0% 100.0%
FESCAR-37 com.alibaba.fescar.core.rpc.RpcContext 92.4% 94.6% 86.8% 91.2% 0.0% 0.0%
FESCAR-41 com.alibaba.fescar.core.rpc.netty.RmRpcClient 1.7% 1.7% 2.0% 2.0% 0.0% 2.4%
FESCAR-42 com.alibaba.fescar.core.rpc.DefaultServerMessageListenerImpl 24.3% 42.6% 11.8% 27.1% 12.1% 25.4%
FESCAR-5 com.alibaba.fescar.core.protocol.MessageFuture 98.6% 99.1% 96.0% 98.0% 99.2% 100.0%
FESCAR-6 com.alibaba.fescar.core.rpc.netty.TmRpcClient 3.4% 3.4% 2.7% 2.7% 0.0% 2.7%
FESCAR-7 com.alibaba.fescar.core.rpc.netty.MessageCodecHandler 76.1% 78.2% 73.3% 77.2% 0.0% 0.0%
FESCAR-8 com.alibaba.fescar.core.rpc.netty.NettyPoolableFactory 57.3% 62.0% 50.8% 57.5% 0.0% 0.0%
FESCAR-9 com.alibaba.fescar.core.protocol.transaction.GlobalBeginRequest 99.0% 98.3% 100.0% 100.0% 99.1% 98.2%
GUAVA-102 com.google.common.collect.LinkedListMultimap 29.4% 32.3% 12.9% 11.6% 19.2% 14.8%
GUAVA-110 com.google.common.collect.LexicographicalOrdering 3.0% 22.2% 0.0% 7.5% 0.6% 15.0%
GUAVA-128 com.google.common.base.Throwables 75.1% 25.0% 75.8% 25.3% 81.0% 26.8%
GUAVA-129 com.google.common.collect.SparseImmutableTable 31.9% 35.8% 37.5% 42.5% 35.0% 43.8%
GUAVA-159 com.google.common.primitives.ParseRequest 100.0% 100.0% 100.0% 100.0% 50.0% 50.0%
GUAVA-169 com.google.common.math.LongMath 96.2% 86.7% 94.2% 85.3% 99.2% 89.3%
GUAVA-177 com.google.common.primitives.Doubles 98.7% 98.5% 99.3% 99.3% 100.0% 100.0%
GUAVA-181 com.google.common.primitives.SignedBytes 100.0% 100.0% 100.0% 100.0% 100.0% 100.0%
GUAVA-184 com.google.thirdparty.publicsuffix.PublicSuffixType 100.0% 100.0% 100.0% 100.0% 100.0% 100.0%
GUAVA-196 com.google.common.io.Closeables 71.5% 70.0% 77.5% 75.0% 88.0% 88.0%
GUAVA-2 com.google.common.collect.MinMaxPriorityQueue 13.9% 22.5% 6.4% 11.1% 16.5% 19.2%
GUAVA-206 com.google.common.collect.ImmutableEnumSet 25.4% 26.1% 23.6% 24.5% 7.1% 7.6%
GUAVA-212 com.google.common.net.MediaType 92.6% 94.3% 77.6% 83.0% 0.0% 0.0%
GUAVA-22 com.google.common.graph.Graphs 53.9% 49.7% 51.8% 47.3% 0.0% 0.0%
GUAVA-224 com.google.common.primitives.UnsignedLongs 99.3% 89.6% 100.0% 90.0% 100.0% 90.0%
GUAVA-240 com.google.common.collect.FilteredMultimapValues 12.3% 22.7% 0.0% 5.0% 0.0% 0.0%
GUAVA-39 com.google.common.collect.TreeMultiset 30.2% 43.1% 18.6% 27.9% 19.5% 31.3%
GUAVA-47 com.google.common.collect.FilteredEntryMultimap 2.6% 11.3% 0.0% 0.7% 0.0% 0.4%
GUAVA-90 com.google.common.io.FileBackedOutputStream 98.9% 89.6% 98.1% 90.0% 98.0% 89.3%
GUAVA-95 com.google.common.collect.ComparatorOrdering 27.5% 51.7% 12.5% 30.0% 18.8% 31.2%
PDFBOX-117 org.apache.pdfbox.filter.Predictor 89.0% 93.5% 83.9% 91.0% 0.0% 28.6%
PDFBOX-127 org.apache.pdfbox.pdfparser.PDFObjectStreamParser 57.5% 65.6% 37.1% 43.6% 44.4% 50.6%
PDFBOX-130 org.apache.pdfbox.pdmodel.interactive.digitalsignature.visible.PDVisibleSignDesigner 7.1% 14.3% 1.7% 1.7% 1.5% 2.5%
PDFBOX-157 org.apache.pdfbox.pdmodel.font.PDType1Font 2.1% 0.0% 0.4% 0.0% 0.0% 0.0%
PDFBOX-198 org.apache.pdfbox.pdmodel.fdf.FDFAnnotationLine 66.4% 66.5% 32.4% 32.7% 5.5% 0.0%
PDFBOX-214 org.apache.pdfbox.pdfparser.EndstreamOutputStream 99.5% 90.0% 99.2% 90.0% 48.0% 40.0%
PDFBOX-22 org.apache.pdfbox.pdmodel.fdf.FDFAnnotationCaret 63.9% 63.9% 64.3% 64.3% 10.5% 31.4%
PDFBOX-220 org.apache.pdfbox.filter.JPXFilter 32.7% 32.7% 7.7% 7.3% 0.0% 0.0%
PDFBOX-229 org.apache.pdfbox.util.XMLUtil 62.4% 69.6% 52.5% 60.0% 10.7% 13.6%
PDFBOX-234 org.apache.pdfbox.pdmodel.interactive.action.PDActionSound 97.7% 96.7% 88.9% 87.8% 0.0% 20.0%
PDFBOX-235 org.apache.pdfbox.pdmodel.font.PDTrueTypeFontEmbedder 0.0% 0.0% 0.0% 0.0% 0.0% 0.0%
PDFBOX-26 org.apache.pdfbox.pdmodel.encryption.SecurityProvider 55.8% 56.8% 100.0% 100.0% 100.0% 90.0%
PDFBOX-265 org.apache.pdfbox.pdmodel.font.PDType3Font 62.4% 70.2% 42.3% 52.0% 0.0% 0.0%
PDFBOX-278 org.apache.pdfbox.pdfwriter.ContentStreamWriter 96.8% 98.3% 96.7% 96.3% 0.0% 0.0%
PDFBOX-285 org.apache.pdfbox.pdmodel.interactive.digitalsignature.PDSignature 98.9% 99.7% 89.5% 95.5% 0.0% 0.0%
PDFBOX-40 org.apache.pdfbox.pdmodel.font.PDCIDFontType2 57.2% 54.9% 45.1% 46.6% 0.0% 0.0%
PDFBOX-62 org.apache.pdfbox.rendering.PageDrawer 2.3% 6.8% 1.2% 4.2% 0.0% 0.0%
PDFBOX-8 org.apache.pdfbox.pdmodel.font.FileSystemFontProvider 45.2% 48.4% 34.2% 35.8% 41.9% 52.2%
PDFBOX-83 org.apache.pdfbox.contentstream.operator.text.SetTextRenderingMode 89.3% 85.7% 92.5% 100.0% 82.5% 87.5%
PDFBOX-91 org.apache.pdfbox.pdmodel.documentinterchange.taggedpdf.PDArtifactMarkedContent 91.6% 97.9% 71.2% 92.5% 0.0% 0.0%
SPOON-105 spoon.support.compiler.jdt.PositionBuilder 9.6% 5.5% 7.8% 3.9% 0.0% 0.0%
SPOON-155 spoon.reflect.visitor.filter.AllMethodsSameSignatureFunction 13.0% 12.7% 0.0% 1.2% 0.7% 3.2%
SPOON-16 spoon.reflect.path.CtElementPathBuilder 15.9% 16.1% 8.0% 9.0% 10.3% 6.4%
SPOON-169 spoon.reflect.visitor.ImportScannerImpl 1.2% 10.6% 0.1% 4.7% 0.0% 1.3%
SPOON-20 spoon.support.reflect.reference.CtLocalVariableReferenceImpl 30.0% 38.6% 14.0% 18.0% 3.3% 13.3%
SPOON-211 spoon.reflect.path.impl.CtRolePathElement 16.3% 18.3% 6.2% 10.3% 6.2% 11.2%
SPOON-25 spoon.pattern.internal.ValueConvertorImpl 3.0% 7.1% 1.2% 3.1% 0.7% 4.3%
SPOON-253 spoon.pattern.internal.parameter.MapParameterInfo 76.8% 73.9% 72.5% 73.8% 0.0% 0.0%
SPOON-32 spoon.MavenLauncher 27.0% 30.0% 11.2% 12.5% 6.0% 6.7%
SPOON-65 spoon.support.DefaultCoreFactory 10.7% 9.7% 5.9% 8.9% 0.1% 0.0%
"""

print(r.count('\n'))